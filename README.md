# 🌐 팀 Lavender - Netchury

> **일반인도 간단하게 사용할 수 있는 네트워크 보안 프로그램, Netchury입니다.**

---

## 📌 프로젝트 개요

### 🔹 배경
최근 네트워크 해킹 공격이 기하급수적으로 증가하면서 보안에 대한 경각심이 커지고 있습니다.  
하지만 기존 보안 프로그램은 기업 중심으로 설계되어 일반 개인이 사용하기엔 기능이 복잡하고 설정이 어려운 경우가 많습니다.  

이에 **팀 Lavender**는  
**“일반 개인도 쉽게 사용할 수 있는 네트워크 보안 프로그램”** 을 목표로 Netchury를 개발하게 되었습니다.

---

### 🔹 네트워크 보안 프로그램이란?

네트워크 보안 프로그램은 네트워크 상의 데이터 송수신을 분석하고,  
이상 징후나 공격 시도를 탐지 및 차단하는 소프트웨어입니다.

---

### 🔹 목표

1. **👤 개인 사용자 친화성**  
   보안/네트워크에 대한 전문성이 없는 개인 사용자도 쉽게 쓸 수 있도록 단순한 UI와 기능을 제공합니다.

2. **🛡️ 정확한 이상 징후 탐지**  
   모의해킹을 통한 데이터 수집 및 분석으로 보안 위협을 정확히 탐지할 수 있도록 설계되었습니다.  

   공격자 화면 | 피해자 화면
   ---|---
   ![공격자 화면](https://puzzling-hamster-b6a.notion.site/image/attachment%3Adc53b5e5-a467-49c6-8a72-f2e282166f43%3A%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-14_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_3.25.18.png?table=block&id=270a10a2-7f0b-80dc-a6ef-db974d9dd9a4&spaceId=7eae2d79-7f2f-4ca8-bc3b-efad9ed3829d&width=640&userId=&cache=v2) | ![피해자 화면](https://puzzling-hamster-b6a.notion.site/image/attachment%3Acbf4cf4c-1621-4659-bd13-81c1ab1d7a19%3A%E1%84%8B%E1%85%B5%E1%86%B7%E1%84%92%E1%85%A7%E1%86%AB%E1%84%8B%E1%85%AE.png?table=block&id=270a10a2-7f0b-8070-81c5-dfa57f3fc2cf&spaceId=7eae2d79-7f2f-4ca8-bc3b-efad9ed3829d&width=640&userId=&cache=v2)

3. **⚡ 최적화된 성능**  
   모든 프로세스를 로컬에서 실행하며, 지속적으로 성능 테스트를 통해 최적화하고 있습니다.

---

### 🔹 결론

> **Netchury = 개인 사용자 친화성 + 정확한 탐지 + 최적화된 성능**  

Lavender 팀은 앞으로도 사용자 경험과 성능 향상을 지속적으로 개선해  
개인 사용자의 네트워크 보안을 한층 강화할 계획입니다.

---

## 📊 Pages

### 📡 Traffic Page
네트워크 활동을 직관적으로 시각화하여 보여주는 페이지입니다.  
- 실시간 입출력 데이터량 모니터링  
- 송·수신 속도 그래프 표시  
- 구간별 네트워크 집중 사용량 확인  
- 총합(KB 단위), 누적치, 실시간 전송 속도(KB/s) 제공  

![Traffic Page](https://puzzling-hamster-b6a.notion.site/image/attachment%3A668e5558-8f44-491c-bf90-03a083ca10e6%3Aimage.png?table=block&id=26fa10a2-7f0b-8057-a61e-cd0135d09e3e&spaceId=7eae2d79-7f2f-4ca8-bc3b-efad9ed3829d&width=1420&userId=&cache=v2)

---

### 🚫 Blocked IP List Page
차단된 IP 주소를 한눈에 확인하고 관리할 수 있는 페이지입니다.  
- Blocked / Allowed 여부 색상 및 아이콘 표시  
- 수동 차단 및 해제 기능 제공  
- 반복 공격 패턴 분석 및 정책 개선 지원  

![Blocked IP List](https://puzzling-hamster-b6a.notion.site/image/attachment%3A4daf8bb1-fb9a-4e13-b6dc-0810ab703ea3%3Aimage.png?table=block&id=26fa10a2-7f0b-803e-afc2-c81b2dfe17e8&spaceId=7eae2d79-7f2f-4ca8-bc3b-efad9ed3829d&width=1420&userId=&cache=v2)

---

### 📜 Net Logs Page
네트워크 이상 징후 및 의심스러운 활동을 기록/표시하는 페이지입니다.  
- 보안 위협 빠른 파악  
- 공격 기록 및 대응 근거 확보  

![Net Logs](https://puzzling-hamster-b6a.notion.site/image/attachment%3A72f14908-718e-4e69-9ec8-280746bffc20%3Aimage.png?table=block&id=26fa10a2-7f0b-8021-ac6a-c89f350904d7&spaceId=7eae2d79-7f2f-4ca8-bc3b-efad9ed3829d&width=1420&userId=&cache=v2)

---

## 🛠 기술 스택

- **Language**: Python  
- **UI**: [PySide6] – 사용자 인터페이스 구현  
- **DB**: [sqlite3] – Blocked/Allowed IP 저장  
- **Network**: [psutil] – 네트워크 데이터 측정  

---

## 👥 팀 구성원

| 역할 | 이름 |
|------|------|
| 🎨 Product Manager / Designer | [김정현](https://github.com/vlsvita) |
| 💻 Developer | [임현우](https://github.com/imhyeonu826) |
| 💻 Developer | [유을](https://github.com/skwo27) |
| 💻 Developer | [김동현](https://github.com/kdh1123) |
| 💻 Developer | [심서훈](https://github.com/Simseoh) |
| 📝 Planner | [김현준](https://github.com/insu6322) |
| 💻 Developer | [이경민](https://github.com/sitetamp) |

---

## 📢 마무리

> Netchury는 개인 사용자의 보안에 최적화된 **차세대 네트워크 보안 프로그램** 입니다.  
> 저희 팀 Lavender는 앞으로도 보안성과 편의성을 개선해 나가겠습니다. 🚀
