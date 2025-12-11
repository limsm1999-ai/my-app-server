# APK 다운로드 서버

QR 코드로 APK를 배포하기 위한 서버입니다.

## 📁 파일 구조

```
apk-server/
├── app.py          # 서버 코드
├── requirements.txt # 의존성
├── app.apk         # ⚠️ 여기에 본인 APK 파일 추가!
└── README.md       # 설명서
```

## 🚀 배포 방법 (Render)

### 1단계: GitHub에 올리기

1. [github.com](https://github.com) 로그인
2. 우측 상단 `+` → `New repository` 클릭
3. Repository name: `apk-server` 입력
4. `Public` 선택
5. `Create repository` 클릭
6. `uploading an existing file` 클릭
7. 이 폴더의 모든 파일 + **본인 APK 파일(이름을 app.apk로 변경)** 드래그해서 업로드
8. `Commit changes` 클릭

### 2단계: Render에서 배포

1. [render.com](https://render.com) 접속
2. GitHub 계정으로 로그인
3. 우측 상단 `New +` → `Web Service` 클릭
4. `Build and deploy from a Git repository` 선택
5. 방금 만든 `apk-server` 저장소 선택
6. 설정:
   - **Name**: 원하는 이름 (예: my-app-download)
   - **Region**: Singapore (Southeast Asia)
   - **Branch**: main
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
7. **Free** 플랜 선택
8. `Create Web Service` 클릭

### 3단계: QR 코드 생성

1. 배포 완료되면 URL 받음: `https://my-app-download.onrender.com`
2. [qrcode-monkey.com](https://www.qrcode-monkey.com) 접속
3. URL 입력 후 QR 생성
4. 다운로드!

## 📱 사용자 경험

1. 사용자가 QR 코드 스캔
2. 다운로드 페이지 표시
3. 다운로드 버튼 클릭
4. APK 자동 다운로드
5. 설치!

## ⚠️ 주의사항

- APK 파일 이름을 반드시 `app.apk`로 변경하세요
- 무료 플랜은 15분 비활성시 슬립모드 (첫 접속시 30초 대기)
- Android에서 "출처를 알 수 없는 앱" 설치 허용 필요

## 🔗 유용한 링크

- GitHub: https://github.com
- Render: https://render.com
- QR 생성: https://www.qrcode-monkey.com
