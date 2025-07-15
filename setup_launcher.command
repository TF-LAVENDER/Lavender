#!/bin/bash

echo "Lavender 실행 파일 설정을 시작합니다..."

# 실행 파일 생성
cat > run_lavender.command << 'EOF'
#!/bin/bash

# 현재 스크립트의 디렉토리로 이동
cd "$(dirname "$0")"

# Python 가상환경이 있다면 활성화 (선택적)
# source venv/bin/activate

# Lavender 프로젝트 디렉토리로 이동
cd /Users/dgsw48/PycharmProjects/Lavender

# LavenderMain.py 실행
python3 LavenderMain.py
EOF

# 실행 권한 부여
chmod +x run_lavender.command

# 바탕화면으로 복사
cp run_lavender.command ~/Desktop/

echo "설정이 완료되었습니다!"
echo "바탕화면에서 'run_lavender.command' 파일을 더블클릭하여 프로그램을 실행할 수 있습니다." 

//chmod +x setup_launcher.command   <- 우선 터미널에 이 명령어 실행