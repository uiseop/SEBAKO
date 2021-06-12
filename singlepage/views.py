import json

import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from web3 import Web3

from accounts.decorators import login_message_required
from accounts.models import SNS, Profile, Person
from managepage.views import getCertificationId, getCareerId, getEducationId, certifi_contract, getCompanyId
from resumes.models import SelfIntro, Experience, Education, Resume
from singlepage.forms import snsForm, ProfileForm, ResumeForm, ExperienceForm, EduForm

from bs4 import BeautifulSoup


def _page_id(request):
    single = request.session.session_key
    if not single:
        single = request.session.create()
    return single

url = 'https://ropsten.infura.io/v3/93d5193aae28437684c118ba0f6541d6'
web3 = Web3(Web3.HTTPProvider(url))
abi2 = json.loads('''[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "cid",
				"type": "address"
			}
		],
		"name": "newCareerCreated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "pid",
				"type": "address"
			}
		],
		"name": "newCertificationCreated",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "eid",
				"type": "address"
			}
		],
		"name": "newEducationCreated",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "careerList",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "job",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "compName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "content",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "startDate",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "endDate",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "careeID",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "companyAddress",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "cidAvailable",
				"type": "bool"
			},
			{
				"internalType": "bool",
				"name": "companySignature",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "certificationList",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "certiName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "certiNumb",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "compName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "accDate",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "certiID",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "companyAddress",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "pidAvailable",
				"type": "bool"
			},
			{
				"internalType": "bool",
				"name": "companySignature",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "cidCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "cidList",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "compAddressList",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "companyCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "companyDetailList",
		"outputs": [
			{
				"internalType": "address",
				"name": "compAdress",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "compName",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "companyList",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			}
		],
		"name": "companyRejectCaree",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			}
		],
		"name": "companyRejectCerti",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			}
		],
		"name": "companyRejectEdu",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			}
		],
		"name": "companySignCaree",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			}
		],
		"name": "companySignCerti",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_pid",
				"type": "address"
			}
		],
		"name": "companySignEdu",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "educationList",
		"outputs": [
			{
				"internalType": "string",
				"name": "name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "schoolName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "major",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "gpa",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "accDate",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "eduID",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "companyAddress",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "eidAvailable",
				"type": "bool"
			},
			{
				"internalType": "bool",
				"name": "companySignature",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "eidCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "eidList",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "pidCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "pidList",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "renounceOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_job",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_compName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_content",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_startDate",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_endDate",
				"type": "string"
			}
		],
		"name": "setCareerData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_certiName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_certiNumb",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_compName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_accDate",
				"type": "string"
			}
		],
		"name": "setCertificationData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_compAddress",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			}
		],
		"name": "setCompany",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_schoolName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_major",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_gpa",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_accDate",
				"type": "string"
			}
		],
		"name": "setEducationData",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]''')
abi = json.loads('''[
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "string",
				"name": "_title",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_registerNumber",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_company",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_dDate",
				"type": "string"
			}
		],
		"name": "createCertification",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "certificationCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "certifications",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "id",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "title",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "registerNumber",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "company",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "dDate",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "get_count",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	}
]''')

certifi_address = '0xED111aBCE5A36F48bed94B18a995D78B4069f1b5'
contract_address = '0xCB8D8a589623d2DE83D1a5FfCE1759A5947a5F1d'
contract_address = web3.toChecksumAddress(contract_address)
certifi_address = web3.toChecksumAddress(certifi_address)

contract = web3.eth.contract(address=contract_address,abi=abi)
certifi_contract = web3.eth.contract(address=certifi_address,abi=abi2)


# person은 작성자로 념겨줌.
# user은 현재 세션상 로그인한 사용자 정보임.

# @login_required
@login_message_required
def PageDetail(request, pk):
    # print(request.user) : seop 출럭
    # print(request.user.profile.korName)
    person = get_object_or_404(Person, pk=pk)
    profile = get_object_or_404(Profile,user_id=person)
    # user = User.objects.get(id=pk)
    # print(user) : seop 출력
    # print(request.user.id) : 1출력 (첫번째 회원가입한곳)
    intros = SelfIntro.objects.all()
    intro_list = intros.filter(user_id=pk)
    expers = Experience.objects.all()
    experience_list = expers.filter(user_id=pk)
    edus = Education.objects.all()
    education_list = edus.filter(user_id=pk)
    resumes = Resume.objects.all()
    resume_list = resumes.filter(user_id=pk)
    certificationList = []
    careerList = []
    educationList = []
    # pids = getCertificationId()
    # cids = getCareerId()
    # eids = getEducationId()
    # for pid in pids:
    #     certification = certifi_contract.functions.certificationList(pid).call()
    #     certificationList.append(certification)
    #
    # # for cid in cids:
    # #     career = certifi_contract.functions.careerList(cid).call()
    # #     careerList.append(career)
    # #
    # # for eid in eids:
    # #     education = certifi_contract.functions.educationList(eid).call()
    # #     educationList.append(education)
    #
    new_list = []
    new_clist = []
    new_elist = []
    # for data in certificationList:
    #     if profile.korName != '':
    #         if data[0] == profile.korName:
    #             new_list.append(data)
    #         else:
    #             continue
    #
    # for data in careerList:
    #     if profile.korName != '':
    #         if data[0] == profile.korName:
    #             new_clist.append(data)
    #         else:
    #             continue
    #
    # for data in educationList:
    #     if profile.korName != '':
    #         if data[0] == profile.korName:
    #             new_elist.append(data)
    #         else:
    #             continue

    context = {
        "datas":new_list,
        "cdatas":new_clist,
        "edatas":new_elist,
        "person":person,
        "profile":profile,
        "intro_list":intro_list,
        "experience_list":experience_list,
        'education_list': education_list,
        'resume_list': resume_list
    }

    return render(request, 'singlepage/index.html',context)




@method_decorator(login_message_required, name='dispatch')
class snsCreate(CreateView):
    model = SNS
    fields = ['name', 'url']
    template_name = 'singlepage/sns_create.html'

    def form_valid(self, form):
        # print(self.request.user.id) : 1이 출력
        # print(self.request.user) : seop이 출력
        # # 작성자는 현재 로그인 한 사용자로 설정함
        form.instance.user_id = self.request.user

        if form.is_valid():
            form.instance.save()
        else:
            pass

        return redirect('singlepage:page_detail', self.request.user.id)


@login_message_required
def create_sns(request, pk):
    form = snsForm(request.POST)
    if form.is_valid():
        sns = form.save(commit=False)
        # commit=False일 경우 실제 DB에는 적용X
        # 아직 작성자 정보가 없으니


def create_resume(request, pk):
    compList = []
    compids = getCompanyId()

    for comp in compids:
        company = certifi_contract.functions.companyDetailList(comp).call()
        compList.append(company)
    llList = []
    for data in compList:
        llList.append(data)

    person = get_object_or_404(Person,pk=pk)
    profile = get_object_or_404(Profile,user_id=person)
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('singlepage:page_detail', request.user.id)
        return render(request, 'singlepage/resume_create.html', {'form': form})
    else:
        form = ResumeForm()
        return render(request, 'singlepage/resume_create.html', {'person':person,'profile':profile,'form': form, 'datas':llList})

def created_resume_db(request):
    # ['title','regiNum','issure','dateAcq','file_hash',]
    print(request.POST)
    print(request.POST)
    user = request.user.person.user
    person = get_object_or_404(Person,user_id=user)
    title = request.POST['title']
    regiNum = request.POST['subtitle']
    issure = request.POST['content']
    dateAcq = request.POST['ddate']
    try:
        # API를 통한 통신이 이뤄졋을 경우
        if request.POST['signature']:
            resume = Resume(
                user=person,
                title=title,
                regiNum=regiNum,
                issure=issure,
                dateAcq=dateAcq,
                signature='True'
            )
            message = resume
            context = {
                'message': message,
            }
            resume.save()
            return HttpResponse(status=201)
    except:
        # 블록체인에 올리기만 했을경우
        resume = Resume(
            user = person,
            title = title,
            regiNum = regiNum,
            issure = issure,
            dateAcq = dateAcq,
        )
        message = resume
        context = {
            'message':message,
        }
        resume.save()
        return HttpResponse(status=201)

def created_career_db(request):
    # let job=$("#job").val();
    # let business=$("#business").val();
    # let work=$("#work").val();
    # let startDay = $("#startDay").val();
    # let finishDay=$("#finishDay").val();

    user = request.user
    print(user)
    print(user)
    print(user)
    print(user)
    person = get_object_or_404(Person,user=user)
    job = request.POST['job']
    business = request.POST['business']
    work = request.POST['work']
    startDay = request.POST['startDay']
    finishDay = request.POST['finishDay']
    career = Experience(
        user=person,
        title=job,
        company=business,
        text=work,
        dateFrom=startDay,
        dateEnd=finishDay
    )
    message = career
    context = {
        'message': message,
    }
    career.save()
    return HttpResponse(status=201)

def create_school_db(request):
    # school = models.CharField(max_length=30, verbose_name='학교명')
    # major = models.CharField(max_length=30, verbose_name='전공명', null=True)
    # # course = models.JSONField( verbose_name='이수과목')
    # dateEnd = models.DateField(verbose_name='종료일')
    # GPA = models.CharField(max_length=5, verbose_name='학점')
    user = request.user
    person = get_object_or_404(Person, user=user)
    school = request.POST['school']
    major = request.POST['major']
    dateEnd = request.POST['startDay']
    GPA = request.POST['gdp']
    edu = Education(
        user=person,
        school=school,
        major=major,
        dateEnd=dateEnd,
        GPA=GPA
    )
    message = edu
    context = {
        'message': message,
    }
    edu.save()
    return HttpResponse(status=201)


# API 를 통한 자격증명 (서버가 맛탱이가 감)
def check_Certificate(request):
    # ['title','regiNum','issure','dateAcq','file_hash',]
    user = request.user.person.user
    person = get_object_or_404(Person,user_id=user)
    profile = get_object_or_404(Profile,user_id=person)
    # name = profile.korName
    regiNumber = request.POST['subtitle']
    company = request.POST['content']
    # url = "http://data.kca.kr/api/v1/cq/certificate/check?apiKey=2fd824fae641032fa79d9db55f3be972cf40be4f703334fb5991e485b40705ab&name=송치윤&no=189010149"

    url22 = "http://data.kca.kr/api/v1/cq/certificate/check?apiKey=2fd824fae641032fa79d9db55f3be972cf40be4f703334fb5991e485b40705ab&name=송치윤"+"&no="+regiNumber
    print(url22)

    res = requests.get(url22)

    soup = BeautifulSoup(res.content,'html.parser')
    print(soup)
    return HttpResponse(soup)

# 자체 DB를 사용하는 방식 (블록체인 네트워크로 대체)
def delete_resume(request, resume_id,pk):
    user = request.user.person.user
    resume = Resume.objects.get(id=resume_id)
    resume.delete()
    return redirect('singlepage:page_detail', pk=pk)

def delete_career(request, career_id,pk):
    user = request.user
    career = Experience.objects.get(id=career_id)
    career.delete()
    return redirect('singlepage:page_detail', pk=pk)

def delete_edu(request, edu_id,pk):
    user = request.user
    edu = Education.objects.get(id=edu_id)
    edu.delete()
    return redirect('singlepage:page_detail', pk=pk)

def create_experience(request, pk):
    compList = []
    compids = getCompanyId()

    for comp in compids:
        company = certifi_contract.functions.companyDetailList(comp).call()
        compList.append(company)
    llList = []
    for data in compList:
        llList.append(data)


    person = get_object_or_404(Person, pk=pk)
    profile = get_object_or_404(Profile, user_id=person)
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            return redirect('singlepage:page_detail', request.user.id)
        return render(request, 'singlepage/experience_create.html', {'form': form, 'profile':profile})
    else:
        form = ExperienceForm()
        print('hahaha')
        return render(request, 'singlepage/experience_create.html', {'form': form, 'profile':profile, 'datas':llList})


def create_edu(request, pk):
    compList = []
    compids = getCompanyId()

    for comp in compids:
        company = certifi_contract.functions.companyDetailList(comp).call()
        compList.append(company)
    llList = []
    for data in compList:
        llList.append(data)

    person = get_object_or_404(Person, pk=pk)
    profile = get_object_or_404(Profile, user_id=person)
    if request.method == 'POST':
        form = EduForm(request.POST)
        if form.is_valid():
            edu = form.save(commit=False)
            edu.user = request.user
            edu.save()
            return redirect('singlepage:page_detail', request.user.id)
        return render(request, 'singlepage/edu_create.html', {'form': form, 'profile':profile})
    else:
        form = EduForm()
        print('hahaha')
        return render(request, 'singlepage/edu_create.html', {'form': form, 'profile':profile, 'datas':llList})

def create_intro(request, pk):
    person = get_object_or_404(Person, pk=pk)
    profile = get_object_or_404(Profile, user_id=person)
    if request.method == 'POST':
        form = EduForm(request.POST)
        if form.is_valid():
            edu = form.save(commit=False)
            edu.user = request.user
            edu.save()
            return redirect('singlepage:page_detail', request.user.id)
        return render(request, 'singlepage/interests_create.html', {'form': form, 'profile':profile})
    else:
        return render(request, 'singlepage/interests_create.html', {'profile':profile})


@login_message_required
def ChangeProfile(request, pk):
    profile = Profile.objects.get(user_id=pk)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST['name'],request.POST['engName'],request.POST['email'],request.POST['phone'],request.POST['image_hash'],
        request.POST['github'],request.POST['blog'],request.POST['facebook'],request.POST['insta'],instance=profile)
        try: # SNS의 정보를 가져오는것을 먼저 시도해봄
            s = SNS.objects.get(user_id=pk)
            sns_form = snsForm(request.POST, instance=s)

            # sns_form = snsForm(request.POST, instance=sns)
            if profile_form.is_valid() and sns_form.is_valid():
                sns = sns_form.save(commit=False)
                prof = profile_form.save(commit=False)
                sns.save()
                prof.save()
                return redirect('singlepage:page_detail', pk)
            return redirect('singlepage:page_detail', pk)
        except: # 정보가 없으면 새로 추가해주면 됨
            sns = snsForm(request.POST)
            # sns.user_id = pk
            addsns = sns.save(commit=False)
            addsns.user = request.user
            addsns.save()
            return redirect('singlepage:page_detail', request.user.id)

    else:
        # s_form = snsForm(instance=snses[0])
        # sns_form = snsForm(instance=snses[1])
        snses = SNS.objects.all()
        snses = snses.filter(user_id=pk)

        profile_form = ProfileForm(instance=profile)

        if not snses:
            sns1 = snsForm()

            return render(request, 'singlepage/edit_page.html', {'profile_form': profile_form,
                                                                 'sns1_form': sns1,
                                                                 })
        else:
            s = SNS.objects.get(user_id=pk)
            sns_form = snsForm(instance=s)
            # for i in range(len(snses)):
            #     sns[i] = snsForm(instance=snses[i])
            # sns = snsForm(instance=snses)

            # print(profile)
            return render(request, 'singlepage/edit_page.html')


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['korName', 'engName', 'address', 'email', 'phone', 'image', ]
    template_name = 'singlepage/edit_page.html'

    # def get_absolute_url(self):
    #     return reverse('singlepage:page_detail',args=[self.id])

def ProfileCreate(request,pk):
    person = get_object_or_404(Person, pk=pk)
    profile = get_object_or_404(Profile, user_id=person)
    if request.method == 'POST':
        print(request.POST['korName'])
        print(request.POST['korName'])
        print(request.POST['korName'])
        print(request.POST['insta'])
        profile.korName = request.POST['korName']
        profile.engName = request.POST['engName']
        profile.email = request.POST['email']
        profile.phone = request.POST['phone']
        profile.image_hash = request.POST['image_hash']
        profile.github = request.POST['github']
        profile.insta = request.POST['insta']
        profile.blog = request.POST['blog']
        profile.facebook = request.POST['facebook']
        profile.save()
        return redirect('singlepage:page_detail', pk=pk)
    else:
        return render(request, 'singlepage/edit_page.html',
                      {'person':person,'profile':profile})

def append(request):
	return render(request, 'singlepage/submit.html')