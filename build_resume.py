# -*- coding: utf-8 -*-
"""Builds a clean single-column HTML resume with the photo embedded as base64."""
import base64
from pathlib import Path

HERE = Path(__file__).parent
PHOTO = HERE / "김성웅.jpg"
OUT = HERE / "index.html"

with PHOTO.open("rb") as f:
    photo_b64 = base64.b64encode(f.read()).decode("ascii")
photo_url = f"data:image/jpeg;base64,{photo_b64}"

HTML = r"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8" />
<title>김성웅 — AI 개발자 이력서</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
<style>
  :root {
    --ink: #1a1f2b;
    --muted: #5b6473;
    --line: #e6e8ee;
    --accent: #2348a8;
    --soft: #f5f7fb;
    --bg: #ffffff;
    --maxw: 760px;
  }
  * { box-sizing: border-box; }
  html, body {
    margin: 0;
    padding: 0;
    background: #eef1f6;
    color: var(--ink);
    font-family: "Pretendard Variable", Pretendard, -apple-system, BlinkMacSystemFont,
      "Segoe UI", "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;
    font-size: 13px;
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
  }
  .page {
    max-width: var(--maxw);
    margin: 32px auto;
    background: var(--bg);
    box-shadow: 0 6px 24px rgba(20, 30, 60, 0.08);
    border-radius: 12px;
    overflow: hidden;
  }

  /* ===== Header ===== */
  .header {
    display: grid;
    grid-template-columns: 96px 1fr;
    gap: 22px;
    align-items: center;
    padding: 26px 36px 22px 36px;
    border-bottom: 1px solid var(--line);
  }
  .photo {
    width: 96px;
    height: 120px;
    object-fit: cover;
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(20, 30, 60, 0.15);
    background: var(--soft);
  }
  .name {
    margin: 0 0 2px 0;
    font-size: 26px;
    font-weight: 700;
    letter-spacing: -0.02em;
  }
  .name .en {
    font-size: 13px;
    font-weight: 500;
    color: var(--muted);
    margin-left: 6px;
  }
  .role {
    color: var(--accent);
    font-weight: 600;
    font-size: 13.5px;
    margin-bottom: 6px;
    letter-spacing: -0.01em;
  }
  .summary {
    color: var(--muted);
    font-size: 12.5px;
    margin: 0 0 8px 0;
  }
  .contact {
    display: flex;
    flex-wrap: wrap;
    gap: 4px 16px;
    font-size: 12.5px;
  }
  .contact .item { display: inline-flex; align-items: center; gap: 6px; }
  .contact .label { color: var(--muted); }
  .contact a { color: var(--accent); text-decoration: none; }
  .contact a:hover { text-decoration: underline; }

  /* ===== Body ===== */
  .body { padding: 22px 36px 32px 36px; }
  section + section { margin-top: 20px; }

  h2 {
    font-size: 11.5px;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--accent);
    margin: 0 0 12px 0;
    padding-bottom: 6px;
    border-bottom: 1.5px solid var(--accent);
  }
  h3 {
    font-size: 14.5px;
    font-weight: 700;
    margin: 0;
    letter-spacing: -0.01em;
  }

  /* Generic single-row entry: title left, when right */
  .row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 12px;
    margin-bottom: 4px;
  }
  .row .when {
    color: var(--muted);
    font-size: 12.5px;
    white-space: nowrap;
  }
  .sub {
    color: var(--muted);
    font-size: 12.5px;
    margin-bottom: 2px;
  }

  .entry { margin-bottom: 12px; }
  .entry:last-child { margin-bottom: 0; }

  /* ===== Tech stack as horizontal rows ===== */
  .stack-row {
    display: grid;
    grid-template-columns: 110px 1fr;
    gap: 12px;
    align-items: center;
    padding: 6px 0;
    border-bottom: 1px dashed var(--line);
  }
  .stack-row:last-child { border-bottom: none; }
  .stack-row .label {
    font-size: 11.5px;
    font-weight: 700;
    color: var(--muted);
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }
  .chips { display: flex; flex-wrap: wrap; gap: 4px; }
  .chip {
    display: inline-block;
    padding: 2px 8px;
    background: var(--soft);
    color: var(--ink);
    border: 1px solid var(--line);
    border-radius: 999px;
    font-size: 11.5px;
    line-height: 1.5;
  }

  /* ===== Lists for awards, certs, military ===== */
  ul.line-list {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  ul.line-list li {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    padding: 5px 0;
    border-bottom: 1px dashed var(--line);
    font-size: 13px;
  }
  ul.line-list li:last-child { border-bottom: none; }
  ul.line-list .when {
    color: var(--muted);
    font-size: 12px;
    white-space: nowrap;
  }

  /* ===== Projects ===== */
  .project { margin-bottom: 16px; }
  .project:last-child { margin-bottom: 0; }
  .project-org {
    color: var(--muted);
    font-size: 12.5px;
    margin-bottom: 6px;
  }

  /* Sub-projects nested inside an Experience entry */
  .sub-projects {
    margin-top: 10px;
    padding-left: 14px;
    border-left: 2px solid var(--line);
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .sub-projects .project { margin-bottom: 0; }
  .sub-projects h3 { font-size: 13.5px; }
  .sub-projects .lede { font-size: 12px; padding: 6px 10px; }
  .sub-projects ul.bullets li { font-size: 12px; }
  .sub-projects .when { font-size: 12px; }
  .lede {
    color: var(--muted);
    font-size: 12.5px;
    margin: 0 0 6px 0;
    padding: 7px 11px;
    background: var(--soft);
    border-left: 3px solid var(--accent);
    border-radius: 4px;
  }
  ul.bullets {
    margin: 6px 0 0 0;
    padding-left: 18px;
  }
  ul.bullets li {
    margin-bottom: 3px;
    font-size: 12.5px;
    line-height: 1.6;
  }
  ul.bullets li::marker { color: var(--accent); }
  .link-line {
    margin-top: 6px;
    font-size: 12px;
    color: var(--muted);
  }
  .link-line a { color: var(--accent); text-decoration: none; word-break: break-all; }
  .link-line a:hover { text-decoration: underline; }

  /* ===== Print ===== */
  @media print {
    html, body { background: #fff; font-size: 11.5px; }
    .page {
      box-shadow: none;
      border-radius: 0;
      margin: 0;
      max-width: none;
    }
    .header {
      padding: 0 0 6mm 0;
      gap: 14px;
      grid-template-columns: 88px 1fr;
    }
    .photo { width: 88px; height: 108px; }
    .name { font-size: 22px; }
    .body { padding: 6mm 0 0 0; }
    .entry, .project, section { break-inside: avoid; page-break-inside: avoid; }
    h2, h3 { break-after: avoid; page-break-after: avoid; }
    a { color: var(--ink); }
  }
  @page { size: A4; margin: 12mm 16mm; }
</style>
</head>
<body>
  <main class="page">
    <header class="header">
      <img class="photo" src="__PHOTO__" alt="김성웅 프로필 사진" />
      <div>
        <h1 class="name">김성웅<span class="en">Sungwoong Kim</span></h1>
        <div class="role">AI Developer · Physical AI / VLA · Multimodal</div>
        <p class="summary">
          모델 개발을 넘어 실제 환경에서 작동하는 시스템으로 연결하는 데 흥미를 느끼는 개발자.
          CNN, LLM/VLM, VLA 프로젝트를 거치며 시각 이해 → 멀티모달 추론 → 로봇 행동 학습으로
          경험을 확장했고, 현재는 로봇 모방학습 파이프라인을 직접 설계·개선하고 있습니다.
        </p>
        <div class="contact">
          <span class="item"><span class="label">Email</span><a href="mailto:swk5276@gmail.com">swk5276@gmail.com</a></span>
          <span class="item"><span class="label">Phone</span>010-7740-3249</span>
          <span class="item"><span class="label">GitHub</span><a href="https://github.com/swk5276">github.com/swk5276</a></span>
        </div>
      </div>
    </header>

    <div class="body">

      <section>
        <h2>Experience</h2>
        <div class="entry">
          <div class="row">
            <h3>비전스페이스 · 연구원</h3>
            <span class="when">2025.11 — 재직 중</span>
          </div>
          <div class="sub">VLA · ACT 기반 로봇 모방학습 플랫폼 및 산업 도메인 멀티모달 AI 어시스턴트 개발</div>

          <div class="sub-projects">
            <article class="project">
              <div class="row">
                <h3>VLA · ACT 통합 로봇 모방학습 플랫폼</h3>
                <span class="when">2025.11 — 2026.03</span>
              </div>
              <p class="lede">
                로봇 시연 데이터 수집부터 VLA/ACT 정책 학습 · 추론 · 평가 · 데이터 관리까지 전 과정을 통합한
                End-to-End 로봇 시뮬레이션 기반 학습 플랫폼 개발.
              </p>
              <ul class="bullets">
                <li>MuJoCo 기반 SOARM-101 환경에서 Teleoperation과 Jacobian IK Heuristic을 결합한 이중 수집 파이프라인 설계 — 데이터 수집 속도 <strong>40% 향상</strong>.</li>
                <li>LeRobot 오픈소스 커스터마이징으로 SmolVLA · ACT 정책을 연동, 데이터 수집 → 학습 → 추론 → 검증을 단일 환경에 통합 — 실험 모니터링 및 디버깅 시간 <strong>2배 단축</strong>.</li>
                <li>물체 배치 랜덤화 등 Domain Randomization 적용 및 자동 평가 파이프라인 구성으로 시뮬레이션 환경 내 Task 성공률 <strong>80% 이상</strong> 달성.</li>
                <li>VLA/ACT 정책의 반복적 성능 비교를 위한 MuJoCo-WASM 기반 웹 실험 환경 구축 — 실험 운영 효율 향상.</li>
              </ul>
              <div class="link-line">소개 영상 — <a href="https://www.youtube.com/watch?v=jPdjTp4Qb24">youtube.com/watch?v=jPdjTp4Qb24</a></div>
            </article>

            <article class="project">
              <div class="row">
                <h3>산업 도메인 지식 기반 멀티모달 AI 어시스턴트</h3>
                <span class="when">2025.11 — 2026.03</span>
              </div>
              <p class="lede">
                관련 문서(PDF · CSV · TEXT) · 이미지 · 내부 지식베이스를 통합 이해하는 멀티모달 AI 어시스턴트.
                LangGraph 기반 ReAct 에이전트와 Hybrid RAG를 적용한 도메인 특화 QA 시스템 구현.
              </p>
              <ul class="bullets">
                <li>Supervisor – Planner – Agent 3계층 상태 오케스트레이션과 Fail-safe 설계로 자유형 에이전트의 치명 오류인 무한 루프 발생 <strong>0건</strong> 달성.</li>
                <li>질의 의도에 따라 VLM(의미 해석)과 SigLIP(크로스모달 검색) 역할을 분리한 동적 라우팅 파이프라인 구축 — 불필요한 LLM 추론 방지 및 검색 Latency 단축.</li>
                <li>BM25(Keyword) + FAISS(Vector) Hybrid RAG와 Reranker 적용으로 로봇 · 설비 문서 검색 정확도와 근거 기반 응답 품질 향상.</li>
                <li>vLLM · Ollama 기반 Multi-Provider Gateway 자체 구축으로 On-Premise(폐쇄망) 환경 운영 안정성 확보.</li>
              </ul>
            </article>
          </div>
        </div>
      </section>

      <section>
        <h2>Education</h2>
        <div class="entry">
          <div class="row">
            <h3>Microsoft · SW 인공지능 아카데미 1기</h3>
            <span class="when">2025.02 — 2025.09</span>
          </div>
          <div class="sub">수료</div>
        </div>
        <div class="entry">
          <div class="row">
            <h3>인천대학교 · 임베디드시스템공학과</h3>
            <span class="when">~ 2025.02</span>
          </div>
          <div class="sub">학사 졸업</div>
        </div>
      </section>

      <section>
        <h2>Tech Stack</h2>
        <div class="stack-row">
          <div class="label">Languages</div>
          <div class="chips">
            <span class="chip">Python</span><span class="chip">C</span>
          </div>
        </div>
        <div class="stack-row">
          <div class="label">AI</div>
          <div class="chips">
            <span class="chip">PyTorch</span><span class="chip">VLA</span><span class="chip">VLM</span>
            <span class="chip">LLM</span><span class="chip">RAG</span><span class="chip">Agent</span>
          </div>
        </div>
        <div class="stack-row">
          <div class="label">Backend &amp; HW</div>
          <div class="chips">
            <span class="chip">FastAPI</span><span class="chip">Flask</span><span class="chip">Raspberry Pi (MPU)</span>
          </div>
        </div>
        <div class="stack-row">
          <div class="label">Tools</div>
          <div class="chips">
            <span class="chip">Git</span><span class="chip">Slack</span><span class="chip">Jira</span>
          </div>
        </div>
      </section>

      <section>
        <h2>Projects</h2>

        <article class="project">
          <div class="row">
            <h3>VLM/LLM 멀티 에이전트 숏폼 자동 제작 서비스</h3>
            <span class="when">2025.05 — 2025.09</span>
          </div>
          <div class="project-org">멀티모달 입력 → 스토리/이미지/음성 자동 생성 앱</div>
          <p class="lede">
            멀티모달 입력 데이터를 기반으로 스토리 생성 · 이미지 생성 · 음성 합성을 에이전트 단위로 수행해
            숏폼 콘텐츠를 자동 제작하는 앱 서비스 개발.
          </p>
          <ul class="bullets">
            <li>복수 Whisper 모델 병렬 앙상블과 LLM 기반 문맥 복원(Refiner) 로직으로 현장 노이즈 입력에서의 인식 오류 및 Snowball Effect 구조적 차단.</li>
            <li>VLM 캡셔닝 기반 캐릭터 외형 데이터 추출 및 씬 메타데이터 JSON 구조화 — 다중 인물 환경에서의 시각적 일관성 확보 및 프롬프트 재현성 고도화.</li>
            <li>로컬 음성 모델을 Edge-TTS로 대체 후 에이전트 단위 모듈화 — GPU VRAM 병목 해소 및 영상 렌더링 파이프라인 확장성 확보.</li>
          </ul>
          <div class="link-line">소개 영상 — <a href="https://drive.google.com/file/d/1yQp18nDF7NkoutWgeYCF3596cC2sSsw0/view?usp=sharing">drive.google.com</a></div>
        </article>

        <article class="project">
          <div class="row">
            <h3>CNN 기반 다색상 원단 색상 유사도 검출 시스템</h3>
            <span class="when">2024.01 — 2024.06</span>
          </div>
          <div class="project-org">졸업 프로젝트 · MPU 환경 경량 비전 시스템</div>
          <p class="lede">
            MPU 환경에서 다색상 원단의 색상 유사도를 CNN으로 정량 분석해 의사결정 지표를 제공하는 시스템 개발.
          </p>
          <ul class="bullets">
            <li>원단 이미지 <strong>18,000여 장</strong> 촬영 · 라벨링하여 자체 데이터셋 구축, 도메인 특화 전처리 및 증강 적용.</li>
            <li>DBSCAN Clustering으로 복잡한 무늬 속 색상 자동 분류 구현.</li>
            <li>VGG-16 기반 CNN을 경량화해 저사양 하드웨어에 맞게 최적화 (성능 유지, 연산량 큰 폭 감소).</li>
            <li>색상 채널 분리 후 채널별 모델 학습 및 앙상블 적용으로 유사도 검출 정확도 <strong>97.5%</strong> 달성.</li>
          </ul>
        </article>
      </section>

      <section>
        <h2>Awards</h2>
        <ul class="line-list">
          <li><span>DaCon 문맥 기반 문장 순서 예측 — <strong>8위</strong></span><span class="when">2025.05</span></li>
          <li><span>Hecto 중고차 이미지 분류 — <strong>상위 10%</strong></span><span class="when">2025.06</span></li>
          <li><span>DaCon 자갈·암석 분류 — <strong>상위 8%</strong></span><span class="when">2025.04</span></li>
        </ul>
      </section>

      <section>
        <h2>Certifications</h2>
        <ul class="line-list">
          <li><span>Microsoft Azure AI-900</span><span class="when">2025.07</span></li>
          <li><span>OPIc Intermediate Mid 1</span><span class="when">2024.12</span></li>
          <li><span>1종보통운전면허</span><span class="when">2021.04</span></li>
        </ul>
      </section>

      <section>
        <h2>Military</h2>
        <ul class="line-list">
          <li><span>육군 병장 만기 전역</span><span class="when">2019.09 — 2021.04</span></li>
        </ul>
      </section>

    </div>
  </main>
</body>
</html>
"""

OUT.write_text(HTML.replace("__PHOTO__", photo_url), encoding="utf-8")
print(f"wrote: {OUT}  ({OUT.stat().st_size:,} bytes)")
