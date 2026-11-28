---
title: "Cohere와 Langchain을 활용한 다국어 시맨틱 검색 | Cohere 블로그"
source: "Cohere Blog"
url: "https://cohere.com/ko/blog/search-cohere-langchain"
scraped: "2026-11-28T06:00:15.115339+00:00"
lastmod: "2026-11-27"
type: "sitemap"
---

# Cohere와 Langchain을 활용한 다국어 시맨틱 검색 | Cohere 블로그

**Source**: [https://cohere.com/ko/blog/search-cohere-langchain](https://cohere.com/ko/blog/search-cohere-langchain)

이 글에서는 Cohere 플랫폼과 Langchain을 활용해 다국어 시맨틱 검색을 위한 엔드투엔드 파이프라인을 구축하는 방법을 살펴봅니다. 먼저 문서 목록을 가져와 텍스트 임베딩으로 변환하고, 쿼리와 가장 유사한 문서를 반환하는 기본적인 시맨틱 검색 예제로 시작합니다. 그 다음으로는 기사 같은 장문의 문서에 대한 질문에 답할 수 있는 더 복잡한 애플리케이션을 구축합니다.
위 요약은 Cohere의 새로운 Summarize 베타 엔드포인트를 통해 생성되었으며, 일부 수정되었습니다.
해당 엔드포인트에 대해 여기에서 자세히 알아보세요
.
목차
Cohere 개요
Langchain 개요
다국어 시맨틱 검색 개요
예제 1: 기본 다국어 검색
문서 목록 가져오기
문서 임베딩 및 인덱스 저장
쿼리 입력
쿼리와 가장 유사한 문서 반환
예제 2: 검색 기반 질의응답
기사 추가 및 작은 단락으로 분할
단락 임베딩 및 인덱스 저장
질문 입력
가장 관련성 높은 단락을 기반으로 질문에 답변
소개
Cohere의 대형 언어 모델(LLM)을 기반으로 멋진 애플리케이션을 구축하려는 아이디어가 있으신가요? 하지만 개발을 시작하다 보면, LLM 기반 애플리케이션을 만드는 것이 단순히 모델만 사용하는 것 이상의 작업임을 깨닫게 됩니다. 이를 보완하기 위한 유틸리티를 만들기 시작하지만, 이 과정에 많은 시간이 소요되어 생산성이 저하될 수 있습니다. 사실 머릿속에 떠오르는 아이디어가 너무나 많습니다. 이 아이디어들을 더 효율적으로 구축하고 테스트할 수 있는 방법이 있다면 좋겠습니다.
이 글에서는 Cohere와 Langchain을 통해 이를 어떻게 구현할 수 있는지 살펴보겠습니다.
Cohere 개요
Cohere 플랫폼
은 개발자와 기업이 머신러닝 전문 지식 없이도 최첨단 LLM을 활용할 수 있도록 API를 제공합니다. 이 플랫폼은 방대한 양의 텍스트 데이터를 선별하고, 모델을 개발하며, 분산 학습을 수행하고, 모델을 서비스하는 등 모든 복잡한 과정을 처리합니다. 따라서 개발자는 역량 구축에 시간과 노력을 쏟는 대신, 실제 적용 단계에서 가치를 창출하는 데 집중할 수 있습니다.
Cohere 플랫폼이 제공하는 언어 처리 기능에는 두 가지 핵심 유형이 있습니다. 바로
텍스트 생성
과
텍스트 임베딩
입니다. 각 기능은 서로 다른 유형의 모델로 제공됩니다.
텍스트 생성의 경우, 텍스트 조각 또는
프롬프트
를 입력하면, 프롬프트에 대한 응답으로 생성된 텍스트 스트림을 얻게 됩니다. 예를 들어, 모델에게 하이쿠를 작성하라고 요청(프롬프트)하면, 모델이 직접 작성한 하이쿠(응답 결과)를 반환합니다.
텍스트 임베딩의 경우, 텍스트 조각을 입력하면 해당 텍스트의 시맨틱 의미를 나타내는 숫자 리스트를 얻게 됩니다(시맨틱의 의미는 아래 섹션에서 설명합니다). 이는 텍스트가 나타내는 내용을 "측정"하는 사용 사례, 예를 들어 감성 분석 등에 유용합니다.
Cohere 플랫폼이 제공하는 두 가지 핵심 언어 처리 기능
LangChain 개요
최종 사용자에게 진정한 가치를 제공하기 위해서는 개별 모델만으로는 부족한 경우가 많습니다. 다른 컴퓨팅 리소스나 지식 소스와 결합했을 때 비로소 강력한 앱이 탄생합니다. 바로 이 지점에서
LangChain
이 중요한 역할을 합니다. LangChain은 LLM 기반 애플리케이션을 구축하기 위한 추상화 계층을 제공하는 오픈소스 라이브러리입니다. LangChain은 다양한 모듈을 통해 엔드투엔드 애플리케이션을 쉽고 빠르게 조립할 수 있게 해줍니다. LLM 애플리케이션을 위한 레고 블록이라고 생각하면 됩니다.
이 문서에서는 LangChain의
Chains
및
Indexes
모듈을 사용하여 아주 적은 양의 코드로 엔드투엔드 파이프라인을 구축하는 방법을 설명합니다.
LangChain을 사용하면 LLM 기반 엔드투엔드 애플리케이션을 쉽게 구축할 수 있습니다
다국어 시맨틱 검색 개요
이 문서에서는 다국어 시맨틱 검색에 대해 다룹니다.
먼저, 시맨틱 검색이란 무엇일까요?
시맨틱 검색은 텍스트의 문맥적 의미를 기반으로 검색 기능을 제공합니다. 이는 키워드 검색이라는 대안적 방법의 한계를 해결합니다.
예시를 하나 들어보겠습니다. “먹을 곳”이라는 검색어를 생각해 보겠습니다. 시맨틱 검색 시스템은 이 문구를 “레스토랑”과 연결할 수 있는데, 두 단어의 의미가 비슷하기 때문입니다. 키워드 검색으로는 이런 연결이 불가능하며, 검색 결과도 “먹을”, “곳”이라는 키워드에 국한됩니다.
그렇다면 다국어 검색이란 무엇일까요?
다국어 검색은 검색어와 결과물이 특정 언어에 국한되지 않는 검색 기능입니다. 이러한 시스템을 구축하려면 전통적으로 각 언어별로 개별 파이프라인을 구축해야 하므로, 시스템이 비대해지고 비용도 많이 들며 효율성이 떨어집니다. 하지만
Cohere의 다국어 임베딩 모델
을 사용하면
100개 이상의 언어
를 처리하기 위해 단 하나의 임베딩 모델만 있으면 됩니다.
다국어 모델에 대해 이야기할 때, 다국어 검색과 크로스링구얼 검색이라는 두 가지 유형의 검색이 있습니다.
다국어 검색은 검색어와 결과물이 동일한 언어일 때 이루어집니다. 예를 들어, 영어 검색어 “먹을 곳”에 대해 “Bob's Burgers”라는 영어 결과가 반환되는 경우입니다.
크로스링구얼 검색은 검색어와 결과물이 서로 다른 언어일 때 이루어집니다. 예를 들어, 힌디어 검색어 “खाने की जगह” (먹을 곳)에 대해 “Bob's Burgers”라는 영어 결과가 반환되는 경우입니다.
다국어 검색과 크로스링구얼 검색의 차이점
Cohere의 다국어 임베딩 모델을 사용하면 단 하나의 모델로 다국어 검색과 크로스링구얼 검색 모두를 수행할 수 있습니다. 이 모델이 어떻게 작동하는지 자세히 살펴보겠습니다.
이 문서에 제시된 코드는
Jupyter 노트북
에서 확인할 수 있습니다.
먼저 필요한 패키지를 설치하고, 이 문서에서 사용할 모듈을 임포트합니다. 또한 Cohere API 키를 정의합니다.
! pip install cohere langchain qdrant-client tfds-nightly
from
langchain.embeddings.cohere
import
CohereEmbeddings
from
langchain.llms
import
Cohere
from
langchain.prompts
import
PromptTemplate
from
langchain.text_splitter
import
RecursiveCharacterTextSplitter
from
langchain.chains.question_answering
import
load_qa_chain
from
langchain.chains
import
RetrievalQA
from
langchain.vectorstores
import
Qdrant
from
langchain.document_loaders
import
TextLoader
import
textwrap
as
tr
import
random
import
os
os.environ[
"COHERE_API_KEY"
] =
"COHERE_API_KEY"
예제 1: 기본 다국어 검색
문서 목록에서 가장 관련성 높은 문서를 검색하는 모습
첫 번째 예시에서는 문서 목록에서 가장 관련성 높은 문서를 검색하기 위한 시맨틱 검색 파이프라인을 구축해 보겠습니다. 대표적인 활용 사례로는 팟캐스트나 아티클 추천 시스템이 있습니다.
질문 데이터셋의 문서 목록과 쿼리를 비교하여, 쿼리와 가장 유사한 문서를 반환합니다.
문서는 영어로 되어 있지만, 이 모델이 다국어 검색에서 얼마나 뛰어난 성능을 발휘하는지 확인해 보겠습니다. 5개 언어로 쿼리를 입력하여 결과가 기대치에 부합하는지 살펴보겠습니다.
1단계: 문서 목록 가져오기
먼저, TREC(Tensorflow Datasets 라이브러리에서 공개 제공) 질문 분류 데이터셋에서 질문 목록이 포함된 데이터셋을 가져옵니다.
import
tensorflow_datasets
as
tfds
dataset = tfds.load(
'trec'
, split=
'train'
)
texts = [item[
'text'
].decode(
'utf-8'
)
for
item
in
tfds.as_numpy(dataset)]
이 데이터셋에는 5,452개의 문서가 포함되어 있습니다. 다음은 데이터셋의 샘플 문서들로, 각 문서는 하나의 질문입니다:
신입 변호사의 초봉은 얼마인가요?
빌 게이츠는 어느 대학을 나왔나요?
부비에(Bouvier) 종의 개는 어떤 역할을 하나요?
미국에서 가장 인기 있는 남자 아이 이름은 무엇인가요?
암컷 토끼는 뭐라고 부르나요?
2단계: 문서 임베딩 및 인덱스 저장
이제 핵심 단계로 넘어가겠습니다. 각 문서를
텍스트 임베딩
으로 변환합니다. 이는 텍스트의 문맥과 의미를 수치화한 표현입니다. 이후 이러한 임베딩을 벡터 데이터베이스(인덱스라고도 함)에 저장하여, 시스템이 확장 가능하고 효율적인 방식으로 검색을 수행할 수 있도록 합니다.
Langchain을 사용하면 단 두 줄의 코드로 이를 구현할 수 있습니다.
첫 번째 줄은 임베딩 모델을 정의하며, 여기에서
CohereEmbeddings
객체를 다국어 모델인
multilingual-22-12
로 초기화합니다.
두 번째 줄은 문서를 텍스트 임베딩으로 변환하고 벡터 데이터베이스에 인덱싱합니다. 여러 벡터 데이터베이스 옵션을 사용할 수 있으며, 본 예시에서는 오픈소스 벡터 데이터베이스인 Qdrant를 사용합니다.
여기서는 데이터베이스 위치를 메모리 내로 설정하고 컬렉션 이름을 지정합니다. 또한, 다국어 임베딩 모델은 내적(Dot product) 방식에서 가장 우수한 성능을 발휘하므로 유사도 검색 메서드를 `Dot`으로 설정하는 것이 중요합니다.
# Define the embeddings model
embeddings = CohereEmbeddings(model =
"multilingual-22-12"
)
# Embed the documents and store in index
db = Qdrant.from_texts(texts, embeddings, location=
":memory:"
, collection_name=
"my_documents"
, distance_func=
"Dot"
)
3단계: 쿼리 입력하기
새로운 검색 쿼리를 입력합니다: “빌 게이츠와 연락하는 방법은 무엇인가요?”
이제 문서들을 살펴보면, 세 개의 항목에 “빌 게이츠”라는 용어가 포함되어 있습니다:
마이크로소프트의 빌 게이츠 이메일 주소는 무엇인가요?
빌 게이츠는 어느 대학을 나왔나요?
빌 게이츠의 집은 몇 제곱피트인가요?
이들 중 어느 것도 우리가 찾고 있는 정확한 키워드를 포함하고 있지 않습니다. 일반적인 키워드 검색으로는 이 세 가지 문서 중에서 가장 관련성이 높은 문서를 구분하지 못할 것입니다.
하지만 시맨틱 검색을 사용하면 “get in touch(연락하다)”와 “email address(이메일 주소)”가 유사한 의도를 나타내므로, “마이크로소프트의 빌 게이츠 이메일 주소는 무엇인가요?”라는 문서가 가장 유사한 쿼리로 나타날 것으로 기대할 수 있습니다.
여기서 멈추지 말고 더 살펴봅시다. 다국어 모델은 크로스 랭귀지 작업에서도 뛰어난 성능을 발휘할 수 있습니다. 따라서 동일한 쿼리를 프랑스어와 인도네시아어라는 두 가지 다른 언어로 입력해 보겠습니다.
queries = [
"How to get in touch with Bill Gates"
,
"Comment entrer en contact avec Bill Gates"
,
"Cara menghubungi Bill Gates"
]
queries_lang = [
"English"
,
"French"
,
"Indonesian"
]
모델의 성능을 확인해 보겠습니다.
4단계: 쿼리와 가장 유사한 문서 반환하기
이제 쿼리를 가져와
similarity_search
메서드를 통해 쿼리와 가장 유사한 문서를 가져옵니다. 여기서는 가장 상위에 있는 문서의
page_content
속성을 가져오므로 [0] 인덱스를 사용합니다.
answers = []
for
query
in
queries:
docs = db.similarity_search(query)
answers.append(docs[
0
].page_content)
아래는 영어, 프랑스어, 인도네시아어라는 세 가지 다른 언어로 입력한 쿼리에 대한 결과입니다. 검색 엔진이 쿼리와 의미적으로 가장 유사한 문서를 성공적으로 찾아냈습니다.
쿼리 언어: 영어
쿼리: How to get
in
touch with Bill Gates
가장 유사한 기존 질문: What is Bill Gates of Microsoft E-mail address ?
--------------------
쿼리 언어: 프랑스어
쿼리: Comment entrer en contact avec Bill Gates
가장 유사한 기존 질문: What is Bill Gates of Microsoft E-mail address ?
--------------------
쿼리 언어: 인도네시아어
쿼리: Cara menghubungi Bill Gates
가장 유사한 기존 질문: What is Bill Gates of Microsoft E-mail address ?
--------------------
이 예시에서는 단 몇 줄의 코드로 Langchain을 활용해 시맨틱 검색 시스템을 구축할 수 있는 방법을 살펴보았습니다. 이는 시스템을 처음부터 직접 구축하는 것보다 더 빠릅니다. 이러한 흐름은 다음 예시에서도 이어집니다.
예시 2: 검색 기반 질의응답
긴 문서에 대한 질문에 답변하기
두 번째 예시에서는 시맨틱 검색을 활용해 기사 같은 긴 문서에 대한 질문에 답변하는 방법을 살펴보겠습니다. 여기서는 사용자의 질문을 받아 문서에서 가장 관련성이 높은 문구를 검색하고, 이를 활용해 답변을 생성합니다. 대표적인 적용 사례로는 문서 웹사이트의 검색창이 있습니다.
이번에는 파이프라인에 텍스트 생성 모델을 추가하여 답변 생성 부분을 수행할 수 있도록 하겠습니다.
이해를 돕기 위해 쿼리부터 텍스트 생성까지 모든 과정이 영어로 이루어진 예시를 살펴보겠습니다. 다만, 임베딩 단계에서는 다국어 모델인
multilingual-22-12
모델을 동일하게 사용할 수 있습니다.
1단계: 기사 추가 및 텍스트 분할
예시로 하나의 긴 분량 기사인
스티브 잡스의 2005년 스탠퍼드 대학교 졸업식 연설문
을 사용하겠습니다.
첫 번째 단계는 텍스트를 더 작은 단위로 분할하여 나중에 각 부분을 임베딩할 수 있도록 하는 것입니다. 여기서는 Langchain의
split_documents
메서드를
RecursiveCharacterTextSplitter
모듈에서 사용할 수 있습니다. 분할 단위 크기를 문자 수로 정의할 수 있으며(여기서는 300으로 설정), 분할된 단위들이 일정 길이만큼 겹치도록 설정할 수도 있습니다(여기서는 0으로 설정).
wget
'https://docs.google.com/uc?export=download&id=1f1INWOfJrHTFmbyF_0be5b4u_moz3a4F'
-O steve-jobs-commencement.txt
loader = TextLoader(
"steve-jobs-commencement.txt"
)
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=
500
, chunk_overlap=
0
)
texts = text_splitter.split_documents(documents)
2단계: 텍스트 임베딩 및 인덱스 저장
이 단계는 첫 번째 예시와 동일하며, 각 분할된 텍스트를 동일한 다국어 모델을 사용하여 텍스트 임베딩으로 변환한 후, 이를 벡터 데이터베이스에 인덱싱합니다.
embeddings = CohereEmbeddings(model =
"multilingual-22-12"
)
db = Qdrant.from_documents(texts, embeddings, location=
":memory:"
, collection_name=
"my_documents"
, distance_func=
"Dot"
)
3단계: 질문 입력
다음으로, 답변을 얻고자 하는 질문 목록을 입력합니다. 아래는 우리가 던질 다섯 가지 질문입니다. 앞의 세 가지는 사실에 기반한 답변이 필요한 질문입니다. 네 번째는 정답이 정해져 있지 않은 의견 기반의 질문입니다. 마지막으로 다섯 번째 질문은 문맥상 제공되지 않은 사실 정보를 묻는 질문입니다.
questions = [
"What did the author liken The Whole Earth Catalog to?"
,
"What was Reed College great at?"
,
"What was the author diagnosed with?"
,
"What is the key lesson from this article?"
,
"What did the article say about Michael Jackson?"
,
]
우리가 기대하는 답변을 얻을 수 있는지 확인해 보겠습니다.
4단계: 가장 관련성 높은 텍스트를 기반으로 답변 생성
각 질문에 대해 가장 관련성이 높은 텍스트 분할 단위들을 찾아야 합니다. 여기서는 가장 관련성이 높은 상위 4개의 분할 단위(기본값이며 변경 가능)를 가져오려고 합니다.
이 분할 단위들을 질문 답변의 문맥으로 활용하겠습니다. 문맥이 풍부할수록 텍스트 생성 모델이 더 많은 정보를 활용할 수 있으며, 여기서는
command
모델을 사용하여 답변을 생성합니다.
답변을 생성하려면 텍스트 생성 모델에 다음과 같은 프롬프트를 제공해야 합니다:
생성하고자 하는 내용에 대한 지시 사항
질문과 가장 관련성이 높은 텍스트 조각인 컨텍스트
질문 내용
LangChain을 사용하면
load_qa_chain
메서드를 통해 프롬프트 생성과 텍스트 생성 모델 호출 과정을 하나로 통합할 수 있습니다.
이 메서드는 미리 정의된 프롬프트를 제공하지만,
PromptTemplate
모듈을 사용하여 이를 수정할 수 있습니다. 이 특정 예시의 경우 프롬프트를 수정했을 때 더 나은 결과가 나타났으며, 그 내용은 다음과 같습니다:
prompt_template =
"""Text: {context}
Question: {question}
제공된 텍스트를 바탕으로 질문에 답하세요. 텍스트에 답이 없는 경우, 답을 찾을 수 없다고 답변하세요."""
PROMPT = PromptTemplate(
template=prompt_template, input_variables=[
"context"
,
"question"
]
)
chain_type_kwargs = {
"prompt"
: PROMPT}
그리고 코드는 다음과 같습니다:
qa = RetrievalQA.from_chain_type(llm=Cohere(model=
"command"
, temperature=
0
),
chain_type=
"stuff"
,
retriever=db.as_retriever(),
chain_type_kwargs=chain_type_kwargs,
return_source_documents=
True
)
for
question
in
questions:
answer = qa({
"query"
: question})
아래는 도출된 답변들입니다. 매우 정확해 보입니다!
앞의 세 가지 답변은 시스템이 텍스트에서 추출한 사실 기반의 답변입니다. 네 번째는 개방형 질문으로, 시스템이 텍스트의 내용을 바탕으로 합리적인 답변을 제공했습니다. 다섯 번째 질문 역시 텍스트에 관련 정보가 없음에도 불구하고 정확하게 처리되었습니다.
질문: 저자는
'The Whole Earth Catalog'
를 무엇에 비유했나요?
답변: 구글 등장 35년 전, 구글과 유사한 내용을 담은 페이퍼백 책과 같았습니다.
--------------------
질문: 리드 칼리지(Reed College)는 어떤 점이 뛰어났나요?
답변: 리드 칼리지는 캘리그라피 교육에 탁월했습니다.
--------------------
질문: 저자는 어떤 진단을 받았나요?
답변: 저자는 암 진단을 받았습니다.
--------------------
질문: 이 글의 핵심 교훈은 무엇인가요?
답변: 이 글의 핵심 교훈은 미래에 모든 경험들이 어떻게든 연결될 것이라는 믿음을 가져야 한다는 것입니다. 직관, 운명, 삶, 업보 등 무엇이든 무언가를 믿어야 합니다. 이러한 접근 방식은 저를 실망시킨 적이 없으며, 제 삶에 큰 변화를 가져다주었습니다.
--------------------
질문: 이 글은 마이클 잭슨에 대해 어떻게 언급했나요?
답변: 텍스트에는 마이클 잭슨에 대한 정보가 제공되지 않았습니다.
컨텍스트가 추가된 전체 프롬프트가 어떻게 구성되는지 궁금하시다면, 아래 예시를 참고하세요. 이 예시는 목록의 두 번째 질문인 “저자는 'The Whole Earth Catalog'를 무엇에 비유했나요?”에 대한 프롬프트입니다.
“리드 칼리지의 강점은 무엇이었나요?”에 대한 답변을 생성하기 위한 전체 프롬프트
LangChain에서 디버그 모드를 활성화하면 다음과 같이 이러한 프롬프트를 확인할 수 있습니다:
import
langchain
langchain.debug =
False
마치며
이 글에서는 두 가지 핵심 사항을 살펴보았습니다.
첫 번째는 오늘날 흔히 요구되는 다국어 지원 검색 애플리케이션을 효율적으로 구축하기 위해 단일 다국어 임베딩 모델을 활용하는 방법의 장점입니다. 여러 언어를 지원하기 위해 복잡한 인터페이스와 파이프라인을 구축할 필요가 없습니다. 대신, 하나의 파이프라인으로 100개 이상의 언어를 처리할 수 있습니다.
두 번째는 LangChain 라이브러리와 결합했을 때 이러한 애플리케이션을 구축하는 것이 얼마나 쉽고 효율적인지입니다. Chains, Indexes 등의 모듈을 통해 엔드투엔드 파이프라인 구축 과정이 간소화됩니다.
이 조합은 매우 강력합니다. 이를 통해 다국어 시맨틱 검색 애플리케이션(및 그 이상)을 가장 적은 제약으로 구축하고 수정할 수 있습니다. 효율성이 높을수록 더 많은 실험을 수행할 수 있으며, 실질적인 변화를 가져올 애플리케이션을 더 빠르게 완성할 수 있습니다.
Cohere의 다국어 모델을 사용해 보세요.
여기
서 시작하세요.
Blog
Written By
Meor Amer
Developer Relations
Tags
AI for Developers
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
