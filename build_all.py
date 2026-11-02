import json

with open('questions.json', encoding='utf-8') as f:
    questions_data = json.load(f)

questions_json_str = json.dumps(questions_data, ensure_ascii=False)

# ==========================================
# 1. BUILD index.html
# ==========================================
index_html = f'''<!DOCTYPE html>
<html lang="ja" class="h-full">
<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" name="viewport">
  <title>大和男児か診断</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Firebase SDK (compat) -->
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore-compat.js"></script>
  <script src="firebase-config.js"></script>
  <script id="tailwind-config">
    tailwind.config = {{
      darkMode: "class",
      theme: {{
        extend: {{
          colors: {{
            "surface-tint": "#516071",
            "tertiary-container": "#433628",
            "surface-container-low": "#f2f4f6",
            "on-tertiary-fixed": "#241a0d",
            "secondary-fixed-dim": "#b7c8db",
            "on-secondary-fixed-variant": "#384858",
            "on-background": "#191c1e",
            "on-error-container": "#93000a",
            "surface-container-high": "#e7e8ea",
            "inverse-surface": "#2e3132",
            "on-primary-container": "#94a4b7",
            "tertiary": "#2c2114",
            "inverse-on-surface": "#f0f1f3",
            "on-primary-fixed-variant": "#394859",
            "on-tertiary-fixed-variant": "#524435",
            "on-secondary": "#ffffff",
            "surface-container-lowest": "#ffffff",
            "surface-container-highest": "#e1e2e4",
            "on-surface-variant": "#44474c",
            "on-tertiary-container": "#b19f8c",
            "inverse-primary": "#b8c8dc",
            "primary-container": "#2b3a4a",
            "surface-variant": "#e1e2e4",
            "surface-container": "#edeef0",
            "primary": "#152434",
            "surface": "#f8f9fb",
            "outline": "#74777c",
            "on-tertiary": "#ffffff",
            "primary-fixed-dim": "#b8c8dc",
            "surface-dim": "#d9dadc",
            "on-surface": "#191c1e",
            "secondary": "#4f6070",
            "tertiary-fixed": "#f4dfca",
            "error-container": "#ffdad6",
            "on-secondary-fixed": "#0b1d2b",
            "outline-variant": "#c4c6cc",
            "secondary-container": "#d3e4f8",
            "tertiary-fixed-dim": "#d7c3af",
            "secondary-fixed": "#d3e4f8",
            "primary-fixed": "#d4e4f9",
            "background": "#f8f9fb",
            "on-error": "#ffffff",
            "on-secondary-container": "#556677",
            "surface-bright": "#f8f9fb",
            "on-primary": "#ffffff",
            "error": "#ba1a1a",
            "on-primary-fixed": "#0d1d2c"
          }},
          borderRadius: {{
            "DEFAULT": "0.25rem",
            "lg": "0.5rem",
            "xl": "0.75rem",
            "full": "9999px"
          }},
          spacing: {{
            "space-xl": "2.5rem",
            "margin-desktop": "3rem",
            "space-sm": "0.5rem",
            "gutter-tablet": "1.5rem",
            "margin": "1.25rem",
            "margin-tablet": "2rem",
            "space-xs": "0.25rem",
            "gutter-desktop": "2rem",
            "space-md": "1rem",
            "space-lg": "1.5rem",
            "gutter": "1rem"
          }},
          fontFamily: {{
            "headline-sm": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "body-sm": ["Noto Sans", "sans-serif"],
            "label-lg": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "headline-xl": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "headline-lg": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "headline-xl-mobile": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "label-md": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "headline-lg-mobile": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "label-sm": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "body-lg": ["Noto Sans", "sans-serif"],
            "body-md": ["Noto Sans", "sans-serif"],
            "headline-md": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"]
          }},
          fontSize: {{
            "headline-sm": ["18px", {{ lineHeight: "26px", fontWeight: "500" }}],
            "body-sm": ["13px", {{ lineHeight: "20px", fontWeight: "400" }}],
            "label-lg": ["14px", {{ lineHeight: "20px", fontWeight: "600" }}],
            "headline-xl": ["36px", {{ lineHeight: "44px", fontWeight: "600" }}],
            "headline-lg": ["30px", {{ lineHeight: "38px", fontWeight: "600" }}],
            "headline-xl-mobile": ["28px", {{ lineHeight: "36px", fontWeight: "600" }}],
            "label-md": ["12px", {{ lineHeight: "16px", fontWeight: "500" }}],
            "headline-lg-mobile": ["24px", {{ lineHeight: "32px", fontWeight: "600" }}],
            "label-sm": ["11px", {{ lineHeight: "14px", fontWeight: "500" }}],
            "body-lg": ["17px", {{ lineHeight: "28px", fontWeight: "400" }}],
            "body-md": ["15px", {{ lineHeight: "24px", fontWeight: "400" }}],
            "headline-md": ["20px", {{ lineHeight: "28px", fontWeight: "600" }}]
          }}
        }}
      }}
    }};
  </script>
  <style>
    @layer base {{
      html, body {{
        min-height: 100%;
        margin: 0;
        padding: 0;
        background-color: #f8f9fb;
      }}
      body {{
        overscroll-behavior-y: none;
        -webkit-tap-highlight-color: transparent;
      }}
      .pb-safe {{
        padding-bottom: env(safe-area-inset-bottom, 0px);
      }}
      .pt-safe {{
        padding-top: env(safe-area-inset-top, 0px);
      }}
    }}
    ::-webkit-scrollbar {{
      display: none;
    }}
    .circle-progress {{
      transition: stroke-dashoffset 1.2s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .screen-container {{
      transition: opacity 0.25s ease, transform 0.25s ease;
    }}
    .fade-in {{
      animation: fadeIn 0.3s ease-out forwards;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
  </style>
</head>
<body class="bg-background font-body-md text-on-surface antialiased flex flex-col min-h-screen">

  <!-- Fixed Top Header -->
  <header class="fixed top-0 w-full z-50 pt-safe bg-surface/80 backdrop-blur-xl shadow-[0_1px_8px_rgba(0,0,0,0.04)]">
    <div class="h-14 px-margin max-w-xl mx-auto flex items-center justify-between">
      <h1 id="header-app-title" class="font-headline-sm text-headline-sm text-on-surface tracking-tight text-left truncate font-semibold cursor-pointer select-none" title="トリプルタップで管理者ページへ">
        大和男児か診断
      </h1>
      <span id="header-mode-badge" class="hidden text-[11px] font-label-sm px-2.5 py-0.5 rounded-full bg-surface-container-high text-secondary">
        85問
      </span>
    </div>
  </header>

  <!-- Main Container -->
  <main class="flex-1 flex flex-col relative w-full pt-14 pb-safe bg-surface">

    <!-- ========================================== -->
    <!-- SCREEN 1: START SCREEN (Based on figma/_3) -->
    <!-- ========================================== -->
    <section id="screen-start" class="screen-container flex flex-col w-full max-w-xl mx-auto px-margin pb-space-xl fade-in">
      <div class="py-space-xs"></div>

      <!-- Hero & Title Section -->
      <header class="flex flex-col items-center text-center mt-space-sm mb-space-lg">
        <h1 class="font-headline-xl-mobile text-headline-xl-mobile text-primary tracking-tight font-semibold mb-space-xs">
          大和男児か診断
        </h1>

        <!-- Visual Anchor Motif -->
        <div class="relative w-full max-w-xs h-28 my-space-sm rounded-xl overflow-hidden shadow-sm flex items-center justify-center bg-surface-container-low">
          <div class="absolute -top-10 -right-10 w-32 h-32 rounded-full bg-secondary-container/40 blur-2xl"></div>
          <div class="absolute -bottom-8 -left-8 w-28 h-28 rounded-full bg-primary-fixed/30 blur-xl"></div>
          <div class="relative z-10 flex items-center justify-center gap-space-md">
            <div class="w-12 h-12 rounded-xl bg-surface-container-lowest flex items-center justify-center shadow-sm">
              <span class="material-symbols-outlined text-primary-container text-2xl">neurology</span>
            </div>
            <div class="flex flex-col items-start text-left">
              <span class="font-headline-sm text-headline-sm text-primary font-semibold">8つの行動傾向を解明</span>
              <span class="text-[12px] text-secondary">客観的・多面的な心理分析</span>
            </div>
          </div>
        </div>
      </header>

      <!-- Interactive Input Card -->
      <section class="bg-surface-container-lowest rounded-xl p-space-lg shadow-sm mb-space-md">
        <!-- Step 1: Mode Selection Header -->
        <div class="flex items-center justify-between mb-space-sm">
          <div class="flex items-center gap-space-xs">
            <span class="font-label-sm text-label-sm text-secondary uppercase tracking-wider">Step 01</span>
            <span class="font-label-sm text-label-sm font-semibold text-primary">診断モードを選択</span>
          </div>
        </div>

        <!-- Mode Selection Cards -->
        <div class="grid grid-cols-1 gap-space-xs mb-space-md" id="mode-selector-group">
          <!-- Quick Mode (30 questions) - Selected by default -->
          <div id="mode-quick" class="mode-card is-selected cursor-pointer p-space-sm rounded-lg border transition-all duration-200 bg-surface-container-low border-primary-container shadow-sm flex items-center justify-between gap-space-sm" data-mode="quick">
            <div class="flex items-center gap-space-sm">
              <div class="mode-radio-circle w-5 h-5 rounded-full border border-primary-container flex items-center justify-center transition-colors">
                <div class="mode-radio-dot w-2.5 h-2.5 rounded-full bg-primary-container"></div>
              </div>
              <div class="flex flex-col text-left">
                <div class="flex items-center gap-space-xs">
                  <span class="font-label-lg text-label-lg font-semibold text-primary">クイック診断</span>
                  <span class="px-1.5 py-0.2 rounded text-[10px] font-label-sm bg-primary-fixed text-on-primary-fixed font-semibold">30問</span>
                </div>
                <span class="font-body-sm text-body-sm text-on-surface-variant text-[12px]">約3分・手軽に傾向を把握</span>
              </div>
            </div>
            <span class="material-symbols-outlined text-primary-container text-xl">bolt</span>
          </div>

          <!-- Full Mode (85 questions) -->
          <div id="mode-full" class="mode-card cursor-pointer p-space-sm rounded-lg border transition-all duration-200 bg-surface-container-lowest border-outline-variant/40 hover:border-primary-container/40 flex items-center justify-between gap-space-sm" data-mode="full">
            <div class="flex items-center gap-space-sm">
              <div class="mode-radio-circle w-5 h-5 rounded-full border border-outline-variant flex items-center justify-center transition-colors">
                <div class="mode-radio-dot w-2.5 h-2.5 rounded-full bg-primary-container hidden"></div>
              </div>
              <div class="flex flex-col text-left">
                <div class="flex items-center gap-space-xs">
                  <span class="font-label-lg text-label-lg font-semibold text-primary">精密フル診断</span>
                  <span class="px-1.5 py-0.2 rounded text-[10px] font-label-sm bg-surface-container-high text-secondary">85問</span>
                </div>
                <span class="font-body-sm text-body-sm text-on-surface-variant text-[12px]">約8分・8つの行動傾向を完全解明</span>
              </div>
            </div>
            <span class="material-symbols-outlined text-secondary text-xl">psychology</span>
          </div>
        </div>

        <!-- Step 2: Name Input Header -->
        <div class="flex items-center justify-between mb-space-xs pt-space-xs border-t border-surface-container">
          <div class="flex items-center gap-space-xs">
            <span class="font-label-sm text-label-sm text-secondary uppercase tracking-wider">Step 02</span>
            <span class="font-label-sm text-label-sm font-semibold text-primary">お名前を入力</span>
          </div>
        </div>

        <!-- Input Group -->
        <div class="flex flex-col gap-space-xs mb-space-md">
          <label class="font-label-lg text-label-lg text-primary flex items-center justify-between" for="user-name">
            <span class="text-[13px] text-on-surface-variant">診断結果に表示されるお名前</span>
            <span class="font-label-sm text-label-sm text-outline" id="char-counter">0 / 15</span>
          </label>
          <div class="relative flex items-center w-full">
            <span class="material-symbols-outlined absolute left-space-md text-secondary pointer-events-none text-xl">
              badge
            </span>
            <input class="w-full h-12 pl-11 pr-10 rounded-lg bg-surface-container-low text-primary font-body-md text-body-md placeholder:text-outline-variant outline-none transition-all duration-200 focus:ring-1 focus:ring-primary-container"
              id="user-name" maxlength="15" placeholder="もにん" type="text" value="">
            <button aria-label="名前を消去" class="absolute right-space-sm p-1 text-outline hover:text-primary transition-colors flex items-center justify-center rounded-full opacity-0 pointer-events-none" id="clear-btn" type="button">
              <span class="material-symbols-outlined text-[18px]">cancel</span>
            </button>
          </div>
        </div>

        <!-- Start Action Button -->
        <div class="flex flex-col gap-space-sm">
          <button class="w-full h-12 rounded-lg bg-surface-container-high text-outline font-label-lg text-label-lg flex items-center justify-center gap-space-xs cursor-not-allowed transition-all duration-200" id="start-btn" type="button" disabled>
            <span>診断を開始する</span>
            <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
          </button>
        </div>
      </section>
    </section>

    <!-- ============================================== -->
    <!-- SCREEN 2: QUESTION SCREEN (Based on figma/_2) -->
    <!-- ============================================== -->
    <section id="screen-question" class="screen-container hidden flex-col w-full max-w-xl mx-auto px-margin pb-safe">
      <div class="flex flex-col w-full pb-8">
        <!-- Progress Header Section -->
        <section class="w-full pt-2 pb-4 flex flex-col gap-2">
          <div class="flex items-center justify-between">
            <div class="flex items-baseline gap-2">
              <span id="diag-q-badge" class="inline-flex items-center px-2 py-0.5 rounded-full bg-primary-container text-on-primary-container font-label-sm text-label-sm tracking-widest uppercase">
                設問 1
              </span>
              <div class="flex items-baseline gap-1">
                <span id="diag-current-num" class="font-headline-sm text-headline-sm text-on-surface font-semibold tracking-tight">1</span>
                <span id="diag-total-num" class="font-label-sm text-label-sm text-secondary">/ 85 完了</span>
              </div>
            </div>
            <span id="diag-progress-pct" class="font-label-sm text-label-sm font-semibold text-primary">1%</span>
          </div>
          <!-- Progress Track & Animated Bar -->
          <div class="relative w-full h-2 bg-surface-container-high rounded-full overflow-hidden shadow-inner">
            <div class="h-full bg-primary rounded-full transition-all duration-300 ease-out" id="diag-progress-fill" style="width: 1%;"></div>
          </div>
        </section>

        <!-- Diagnostic Category Archetype Badge -->
        <div class="pt-1 pb-3 flex items-center justify-between">
          <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg bg-surface-container text-on-surface-variant shadow-sm">
            <span id="diag-category-badge" class="font-label-md text-label-md font-medium tracking-tight">
              メリトクラシー
            </span>
          </div>
        </div>

        <!-- Primary Assessment Prompt Container (Fixed min-height with vertically centered text to prevent button shift) -->
        <section class="relative w-full min-h-[185px] sm:min-h-[160px] rounded-xl bg-surface-container-lowest p-6 shadow-md shadow-primary/5 flex flex-col justify-between">
          <div class="flex items-center justify-between">
            <span id="diag-q-index-label" class="font-label-sm text-label-sm text-secondary">Q.1</span>
          </div>
          <!-- Japanese Core Statement (vertically centered) -->
          <div class="relative my-auto py-2 flex items-center justify-center">
            <p id="diag-question-text" class="font-headline-md text-headline-md text-on-surface leading-relaxed tracking-tight text-justify select-none w-full">
              「妥協してFランに進学するくらいなら、何浪してでも高い目標に向けて死に物狂いで勉強すべきである」
            </p>
          </div>
        </section>

        <!-- Answer Selection Nodes (5-Point Likert Scale) -->
        <section aria-label="設問の回答候補" class="w-full flex flex-col gap-2 pt-3 pb-3" role="radiogroup">
          <!-- 1: 同意 (+2) -->
          <button class="option-btn group relative w-full min-h-[48px] sm:min-h-[50px] px-4 py-2 rounded-xl bg-surface-container-lowest text-on-surface shadow-sm hover:shadow active:scale-[0.98] transition-all flex items-center justify-between text-left" data-val="agree" type="button">
            <div class="flex items-center gap-3">
              <div class="status-indicator w-6 h-6 rounded-full bg-surface-container-high flex items-center justify-center transition-colors shrink-0">
                <span class="material-symbols-outlined text-[16px] check-icon transition-opacity opacity-0 text-secondary">check_circle</span>
              </div>
              <div class="flex flex-col">
                <span class="font-label-lg text-[14px] font-semibold tracking-wide">同意</span>
                <span class="font-label-sm text-[11px] text-secondary sub-text">強く同意する・共感</span>
              </div>
            </div>
            <span class="font-label-sm text-[12px] font-bold text-secondary points-badge shrink-0">+2</span>
          </button>

          <!-- 2: やや同意 (+1) -->
          <button class="option-btn group relative w-full min-h-[48px] sm:min-h-[50px] px-4 py-2 rounded-xl bg-surface-container-lowest text-on-surface shadow-sm hover:shadow active:scale-[0.98] transition-all flex items-center justify-between text-left" data-val="somewhat_agree" type="button">
            <div class="flex items-center gap-3">
              <div class="status-indicator w-6 h-6 rounded-full bg-surface-container-high flex items-center justify-center transition-colors shrink-0">
                <span class="material-symbols-outlined text-[16px] check-icon transition-opacity opacity-0 text-secondary">check</span>
              </div>
              <div class="flex flex-col">
                <span class="font-label-lg text-[14px] font-semibold tracking-wide">やや同意</span>
                <span class="font-label-sm text-[11px] text-secondary sub-text">どちらかといえば同意</span>
              </div>
            </div>
            <span class="font-label-sm text-[12px] font-bold text-secondary points-badge shrink-0">+1</span>
          </button>

          <!-- 3: 中立 (0) -->
          <button class="option-btn group relative w-full min-h-[48px] sm:min-h-[50px] px-4 py-2 rounded-xl bg-surface-container-lowest text-on-surface shadow-sm hover:shadow active:scale-[0.98] transition-all flex items-center justify-between text-left" data-val="neutral" type="button">
            <div class="flex items-center gap-3">
              <div class="status-indicator w-6 h-6 rounded-full bg-surface-container-high flex items-center justify-center transition-colors shrink-0">
                <span class="material-symbols-outlined text-[16px] check-icon transition-opacity opacity-0 text-secondary">remove</span>
              </div>
              <div class="flex flex-col">
                <span class="font-label-lg text-[14px] font-semibold tracking-wide">中立</span>
                <span class="font-label-sm text-[11px] text-secondary sub-text">どちらともいえない</span>
              </div>
            </div>
            <span class="font-label-sm text-[12px] font-bold text-secondary points-badge shrink-0">0</span>
          </button>

          <!-- 4: やや反対 (-1) -->
          <button class="option-btn group relative w-full min-h-[48px] sm:min-h-[50px] px-4 py-2 rounded-xl bg-surface-container-lowest text-on-surface shadow-sm hover:shadow active:scale-[0.98] transition-all flex items-center justify-between text-left" data-val="somewhat_disagree" type="button">
            <div class="flex items-center gap-3">
              <div class="status-indicator w-6 h-6 rounded-full bg-surface-container-high flex items-center justify-center transition-colors shrink-0">
                <span class="material-symbols-outlined text-[16px] check-icon transition-opacity opacity-0 text-secondary">close</span>
              </div>
              <div class="flex flex-col">
                <span class="font-label-lg text-[14px] font-semibold tracking-wide">やや反対</span>
                <span class="font-label-sm text-[11px] text-secondary sub-text">どちらかといえば反対</span>
              </div>
            </div>
            <span class="font-label-sm text-[12px] font-bold text-secondary points-badge shrink-0">-1</span>
          </button>

          <!-- 5: 反対 (-2) -->
          <button class="option-btn group relative w-full min-h-[48px] sm:min-h-[50px] px-4 py-2 rounded-xl bg-surface-container-lowest text-on-surface shadow-sm hover:shadow active:scale-[0.98] transition-all flex items-center justify-between text-left" data-val="disagree" type="button">
            <div class="flex items-center gap-3">
              <div class="status-indicator w-6 h-6 rounded-full bg-surface-container-high flex items-center justify-center transition-colors shrink-0">
                <span class="material-symbols-outlined text-[16px] check-icon transition-opacity opacity-0 text-secondary">cancel</span>
              </div>
              <div class="flex flex-col">
                <span class="font-label-lg text-[14px] font-semibold tracking-wide">反対</span>
                <span class="font-label-sm text-[11px] text-secondary sub-text">同意しない・違和感</span>
              </div>
            </div>
            <span class="font-label-sm text-[12px] font-bold text-secondary points-badge shrink-0">-2</span>
          </button>
        </section>

        <!-- Bottom Navigation & Back Button -->
        <section class="mt-2 pt-2 flex flex-col gap-3">
          <div class="flex items-center justify-between gap-3">
            <button id="prev-btn" class="flex-1 h-12 rounded-lg bg-surface-container hover:bg-surface-container-high active:scale-[0.98] transition-all flex items-center justify-center gap-1.5 text-on-surface-variant font-label-md text-label-md" type="button">
              <span class="material-symbols-outlined text-[18px]">arrow_back</span>
              <span>前の設問に戻る</span>
            </button>
          </div>
        </section>
      </div>
    </section>

    <!-- ============================================ -->
    <!-- SCREEN 3: RESULT SCREEN (Based on figma/_1) -->
    <!-- ============================================ -->
    <section id="screen-result" class="screen-container hidden flex-col w-full max-w-xl mx-auto px-margin pb-space-xl">
      <div class="flex flex-col w-full space-y-space-md pt-2">
        <!-- Status Badge & Candidate Identity -->
        <div class="pt-space-xs flex flex-col items-center text-center space-y-space-xs">
          <div>
            <h2 id="result-user-name" class="font-headline-lg-mobile text-headline-lg-mobile text-primary tracking-tight font-semibold">
              もにん さんの診断結果
            </h2>
          </div>
        </div>

        <!-- Primary Score Card (総合大和男児レベル) -->
        <div class="relative overflow-hidden rounded-xl bg-surface-container-lowest p-space-lg shadow-sm">
          <div class="flex items-start justify-between">
            <div class="space-y-1">
              <h3 class="font-headline-md text-headline-md text-primary">大和男児レベル</h3>
            </div>
          </div>

          <!-- Circular / Central Score Display -->
          <div class="my-space-md flex items-center justify-between">
            <div class="flex flex-col">
              <div class="flex items-baseline space-x-1">
                <span class="font-headline-xl text-[56px] leading-none text-primary tracking-tight font-bold" id="score-counter">0</span>
                <span class="font-headline-md text-headline-md text-secondary font-medium">%</span>
              </div>
            </div>

            <!-- SVG Circular Progress Visual -->
            <div class="relative w-24 h-24 flex items-center justify-center">
              <svg class="w-full h-full transform -rotate-90" viewBox="0 0 100 100">
                <circle class="text-surface-container" cx="50" cy="50" fill="transparent" r="40" stroke="currentColor" stroke-width="8"></circle>
                <circle id="score-circle-bar" class="circle-progress text-primary-container" cx="50" cy="50" fill="transparent" r="40" stroke="currentColor" stroke-dasharray="251.2" stroke-dashoffset="251.2" stroke-linecap="round" stroke-width="8"></circle>
              </svg>
              <div class="absolute inset-0 flex flex-col items-center justify-center">
                <span id="result-badge-icon" class="material-symbols-outlined text-primary-container text-[26px]">military_tech</span>
              </div>
            </div>
          </div>

          <!-- Verdict Banner & Classification -->
          <div class="rounded-lg bg-surface-container-low p-space-md space-y-space-xs">
            <div class="flex items-center justify-between">
              <span class="font-label-sm text-label-sm text-secondary">判定区分</span>
              <span id="verdict-tag" class="inline-flex items-center px-3 py-1 rounded-full bg-primary text-on-primary font-label-md text-label-md tracking-wider shadow-sm">
                男前
              </span>
            </div>
            <p id="verdict-summary" class="font-body-sm text-body-sm text-on-surface pt-1 leading-relaxed">
              行動基準がストイックかつ圧倒的な胆力と自己責任マインドを兼ね備えたタイプ。環境を言い訳にせず自己規律を貫徹する精神的自律性が極めて顕著です。
            </p>
            <div class="pt-2 flex items-center justify-between text-secondary font-label-sm text-label-sm border-t-0">
              <span class="flex items-center space-x-1">
                <span class="inline-block w-2 h-2 rounded-full bg-primary-container"></span>
                <span>50%以上: 男前</span>
              </span>
              <span class="flex items-center space-x-1 text-outline">
                <span class="inline-block w-2 h-2 rounded-full bg-surface-container-highest"></span>
                <span>49%以下: 女々しい</span>
              </span>
            </div>
          </div>
        </div>

        <!-- Detailed Dimension Breakdown Card -->
        <div class="rounded-xl bg-surface-container-lowest p-space-lg shadow-sm space-y-space-md">
          <div class="space-y-0.5">
            <div class="flex items-center space-x-2">
              <span class="material-symbols-outlined text-secondary text-[20px]">bar_chart</span>
              <h3 class="font-headline-sm text-headline-sm text-primary">パラメーター分析</h3>
            </div>
          </div>

          <!-- Parameter Horizontal Bar Meters (Populated dynamically) -->
          <div id="parameters-container" class="space-y-space-md pt-space-xs"></div>
        </div>

        <!-- Type Summary & In-Depth Text Card -->
        <div class="rounded-xl bg-surface-container-lowest p-space-lg shadow-sm space-y-space-md">
          <div class="flex items-center space-x-2">
            <span class="material-symbols-outlined text-secondary text-[20px]">insights</span>
            <h3 class="font-headline-sm text-headline-sm text-primary">プロファイル解説</h3>
          </div>
          <div class="space-y-space-sm">
            <div class="p-space-sm rounded-lg bg-surface-container-low space-y-1">
              <span id="profile-headline" class="font-label-sm text-label-sm text-secondary uppercase font-semibold">コア・アドバンテージ</span>
              <p id="profile-description" class="font-body-md text-body-md text-on-surface leading-relaxed"></p>
            </div>
          </div>
        </div>

        <!-- Actions & Sharing Area -->
        <div class="space-y-space-sm pt-space-xs">
          <!-- Primary Share Action -->
          <button id="share-btn" class="w-full h-12 rounded-lg bg-primary-container text-on-primary font-label-lg text-label-lg flex items-center justify-center space-x-2 shadow-sm active:scale-[0.98] transition-transform" type="button">
            <span class="material-symbols-outlined text-[18px]">share</span>
            <span>結果を共有する</span>
          </button>
          <!-- Secondary Re-test Action -->
          <button id="retest-btn" class="w-full h-12 rounded-lg bg-surface-container text-on-surface font-label-lg text-label-lg flex items-center justify-center space-x-2 active:bg-surface-container-high transition-colors" type="button">
            <span class="material-symbols-outlined text-[18px] text-secondary">restart_alt</span>
            <span>もう一度診断する</span>
          </button>
        </div>
      </div>
    </section>

  </main>

  <!-- Application Logic -->
  <script>
    (function () {{
      // --- DATA ---
      const ALL_QUESTIONS = {questions_json_str};

      const CATEGORIES = [
        'ストイシズム',
        '自己責任論',
        'メリトクラシー',
        '体育会的権威主義',
        'マッチョイズム',
        'ルッキズム',
        '優生思想',
        'ナショナリズム'
      ];

      const CATEGORY_DESCRIPTIONS = {{
        'ストイシズム': '感情や安易な欲望に流されず己を律する禁欲的規律',
        '自己責任論': '境遇を言い訳にせず自らの意志と行動で結果を引き受ける覚悟',
        'メリトクラシー': '客観的成果と実力によって序列を決定する厳格な能力主義',
        '体育会的権威主義': '過酷な上下関係や集団の秩序に忠誠を尽くす精神的タフネス',
        'マッチョイズム': '弱音や女々しい言い訳を排し、骨太な胆力と闘争心を尊ぶ気概',
        'ルッキズム': '体型や身だしなみへの怠惰を許さず外見規律を維持する美意識',
        '優生思想': '合理的な生産性と適者生存の原則を重んじる冷徹なリアリズム',
        'ナショナリズム': '自国の伝統と秩序を守り、規律と誇りを最優先する防衛意識'
      }};

      // --- FIREBASE INITIALIZATION ---
      function getFirebaseConfig() {{
        try {{
          const saved = localStorage.getItem('imai_firebase_config');
          if (saved) return JSON.parse(saved);
        }} catch (e) {{}}
        if (window.FIREBASE_CONFIG && window.FIREBASE_CONFIG.projectId) {{
          return window.FIREBASE_CONFIG;
        }}
        return null;
      }}

      let firestoreDb = null;
      try {{
        const cfg = getFirebaseConfig();
        if (cfg && cfg.projectId && typeof firebase !== 'undefined') {{
          if (!firebase.apps.length) {{
            firebase.initializeApp(cfg);
          }}
          firestoreDb = firebase.firestore();
        }}
      }} catch (e) {{
        console.warn('Firebase init warning:', e);
      }}

      async function saveDiagnosisLog(record) {{
        const nowIso = new Date().toISOString();
        const dataToSave = {{
          ...record,
          createdAtStr: nowIso
        }};

        // 1. Always save in local storage as backup
        try {{
          const logs = JSON.parse(localStorage.getItem('imai_diagnoses_log') || '[]');
          logs.unshift({{ ...dataToSave, id: 'local_' + Date.now() }});
          localStorage.setItem('imai_diagnoses_log', JSON.stringify(logs.slice(0, 500)));
        }} catch (e) {{
          console.error('LocalStorage write error:', e);
        }}

        // 2. Save in Firestore if available
        if (firestoreDb) {{
          try {{
            await firestoreDb.collection('diagnoses').add({{
              ...dataToSave,
              createdAt: firebase.firestore.FieldValue.serverTimestamp()
            }});
            console.log('Saved to Firestore successfully');
          }} catch (err) {{
            console.error('Firestore save failed:', err);
          }}
        }}
      }}

      // Secret Admin Access (Triple click title or #admin hash)
      if (window.location.hash === '#admin') {{
        window.location.href = 'admin.html';
      }}
      let titleClicks = 0;
      let titleClickTimer = null;
      const appTitleEl = document.getElementById('header-app-title');
      if (appTitleEl) {{
        appTitleEl.addEventListener('click', () => {{
          titleClicks++;
          clearTimeout(titleClickTimer);
          if (titleClicks >= 3) {{
            titleClicks = 0;
            window.location.href = 'admin.html';
          }} else {{
            titleClickTimer = setTimeout(() => {{ titleClicks = 0; }}, 800);
          }}
        }});
      }}

      // --- STATE ---
      let currentMode = 'quick'; // 'quick' or 'full'
      let userName = 'もにん';
      let activeQuestions = [];
      let currentIndex = 0;
      let userAnswers = {{}}; // key: questionId, value: 'yes' | 'neutral' | 'no'

      // --- DOM REFS ---
      const screenStart = document.getElementById('screen-start');
      const screenQuestion = document.getElementById('screen-question');
      const screenResult = document.getElementById('screen-result');

      const modeQuick = document.getElementById('mode-quick');
      const modeFull = document.getElementById('mode-full');
      const inputName = document.getElementById('user-name');
      const clearBtn = document.getElementById('clear-btn');
      const charCounter = document.getElementById('char-counter');
      const startBtn = document.getElementById('start-btn');
      const headerModeBadge = document.getElementById('header-mode-badge');

      // Question screen elements
      const diagQBadge = document.getElementById('diag-q-badge');
      const diagCurrentNum = document.getElementById('diag-current-num');
      const diagTotalNum = document.getElementById('diag-total-num');
      const diagProgressPct = document.getElementById('diag-progress-pct');
      const diagProgressFill = document.getElementById('diag-progress-fill');
      const diagCategoryBadge = document.getElementById('diag-category-badge');
      const diagQIndexLabel = document.getElementById('diag-q-index-label');
      const diagQuestionText = document.getElementById('diag-question-text');
      const optionButtons = document.querySelectorAll('.option-btn');
      const prevBtn = document.getElementById('prev-btn');

      // Result screen elements
      const resultUserName = document.getElementById('result-user-name');
      const scoreCounter = document.getElementById('score-counter');
      const scoreCircleBar = document.getElementById('score-circle-bar');
      const resultBadgeIcon = document.getElementById('result-badge-icon');
      const verdictTag = document.getElementById('verdict-tag');
      const verdictSummary = document.getElementById('verdict-summary');
      const parametersContainer = document.getElementById('parameters-container');
      const profileHeadline = document.getElementById('profile-headline');
      const profileDescription = document.getElementById('profile-description');
      const shareBtn = document.getElementById('share-btn');
      const retestBtn = document.getElementById('retest-btn');

      // --- MODE SELECTION ---
      function setMode(mode) {{
        currentMode = mode;
        if (mode === 'quick') {{
          modeQuick.classList.add('is-selected', 'bg-surface-container-low', 'border-primary-container', 'shadow-sm');
          modeQuick.classList.remove('bg-surface-container-lowest', 'border-outline-variant/40');
          modeQuick.querySelector('.mode-radio-circle').classList.add('border-primary-container');
          modeQuick.querySelector('.mode-radio-circle').classList.remove('border-outline-variant');
          modeQuick.querySelector('.mode-radio-dot').classList.remove('hidden');

          modeFull.classList.remove('is-selected', 'bg-surface-container-low', 'border-primary-container', 'shadow-sm');
          modeFull.classList.add('bg-surface-container-lowest', 'border-outline-variant/40');
          modeFull.querySelector('.mode-radio-circle').classList.remove('border-primary-container');
          modeFull.querySelector('.mode-radio-circle').classList.add('border-outline-variant');
          modeFull.querySelector('.mode-radio-dot').classList.add('hidden');
        }} else {{
          modeFull.classList.add('is-selected', 'bg-surface-container-low', 'border-primary-container', 'shadow-sm');
          modeFull.classList.remove('bg-surface-container-lowest', 'border-outline-variant/40');
          modeFull.querySelector('.mode-radio-circle').classList.add('border-primary-container');
          modeFull.querySelector('.mode-radio-circle').classList.remove('border-outline-variant');
          modeFull.querySelector('.mode-radio-dot').classList.remove('hidden');

          modeQuick.classList.remove('is-selected', 'bg-surface-container-low', 'border-primary-container', 'shadow-sm');
          modeQuick.classList.add('bg-surface-container-lowest', 'border-outline-variant/40');
          modeQuick.querySelector('.mode-radio-circle').classList.remove('border-primary-container');
          modeQuick.querySelector('.mode-radio-circle').classList.add('border-outline-variant');
          modeQuick.querySelector('.mode-radio-dot').classList.add('hidden');
        }}
      }}

      modeQuick.addEventListener('click', () => setMode('quick'));
      modeFull.addEventListener('click', () => setMode('full'));

      // --- NAME INPUT ---
      function updateNameState() {{
        const val = inputName.value.trim();
        const len = inputName.value.length;
        charCounter.textContent = `${{len}} / 15`;
        if (val.length > 0) {{
          startBtn.disabled = false;
          startBtn.className = 'w-full h-12 rounded-lg bg-primary-container text-on-primary font-label-lg text-label-lg flex items-center justify-center gap-space-xs shadow-md transition-all duration-200 active:scale-[0.98] cursor-pointer';
          clearBtn.classList.remove('opacity-0', 'pointer-events-none');
          clearBtn.classList.add('opacity-100');
        }} else {{
          startBtn.disabled = true;
          startBtn.className = 'w-full h-12 rounded-lg bg-surface-container-high text-outline font-label-lg text-label-lg flex items-center justify-center gap-space-xs cursor-not-allowed transition-all duration-200';
          clearBtn.classList.add('opacity-0', 'pointer-events-none');
          clearBtn.classList.remove('opacity-100');
        }}
      }}

      inputName.addEventListener('input', updateNameState);
      clearBtn.addEventListener('click', () => {{
        inputName.value = '';
        inputName.focus();
        updateNameState();
      }});

      // --- SCREEN NAVIGATION ---
      function showScreen(screen) {{
        [screenStart, screenQuestion, screenResult].forEach(s => {{
          s.classList.add('hidden');
          s.classList.remove('flex', 'fade-in');
        }});
        screen.classList.remove('hidden');
        screen.classList.add('flex', 'fade-in');
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }}

      // Start Diagnosis
      startBtn.addEventListener('click', () => {{
        if (startBtn.disabled) return;
        const nameVal = inputName.value.trim();
        if (!nameVal) return;
        userName = nameVal;
        
        if (currentMode === 'quick') {{
          activeQuestions = ALL_QUESTIONS.filter(q => q.isFast);
        }} else {{
          activeQuestions = [...ALL_QUESTIONS];
        }}

        currentIndex = 0;
        userAnswers = {{}};

        headerModeBadge.textContent = currentMode === 'quick' ? '30問 (クイック)' : '85問 (精密)';
        headerModeBadge.classList.remove('hidden');

        showScreen(screenQuestion);
        renderCurrentQuestion();
      }});

      // --- QUESTION RENDERING (5-Point Likert Scale) ---
      const OPTION_STYLES = {{
        agree: {{
          bg: 'bg-primary',
          text: 'text-on-primary',
          sub: 'text-primary-fixed-dim',
          indicatorBg: 'bg-primary-container',
          indicatorText: 'text-on-primary'
        }},
        somewhat_agree: {{
          bg: 'bg-primary-container',
          text: 'text-on-primary',
          sub: 'text-on-primary-container',
          indicatorBg: 'bg-primary',
          indicatorText: 'text-on-primary'
        }},
        neutral: {{
          bg: 'bg-tertiary-container',
          text: 'text-on-tertiary',
          sub: 'text-on-tertiary-container',
          indicatorBg: 'bg-tertiary',
          indicatorText: 'text-on-tertiary'
        }},
        somewhat_disagree: {{
          bg: 'bg-secondary',
          text: 'text-on-secondary',
          sub: 'text-secondary-fixed',
          indicatorBg: 'bg-surface-container-highest',
          indicatorText: 'text-on-surface'
        }},
        disagree: {{
          bg: 'bg-inverse-surface',
          text: 'text-inverse-on-surface',
          sub: 'text-outline-variant',
          indicatorBg: 'bg-outline',
          indicatorText: 'text-white'
        }},
        // Backwards compatibility for 3-choice records:
        yes: {{
          bg: 'bg-primary',
          text: 'text-on-primary',
          sub: 'text-primary-fixed-dim',
          indicatorBg: 'bg-primary-container',
          indicatorText: 'text-on-primary'
        }},
        no: {{
          bg: 'bg-inverse-surface',
          text: 'text-inverse-on-surface',
          sub: 'text-outline-variant',
          indicatorBg: 'bg-outline',
          indicatorText: 'text-white'
        }}
      }};

      function resetOptionButtons() {{
        optionButtons.forEach(btn => {{
          btn.className = 'option-btn group relative w-full min-h-[48px] sm:min-h-[50px] px-4 py-2 rounded-xl bg-surface-container-lowest text-on-surface shadow-sm hover:shadow active:scale-[0.98] transition-all flex items-center justify-between text-left';
          const sub = btn.querySelector('.sub-text');
          if (sub) sub.className = 'font-label-sm text-[11px] text-secondary sub-text';
          const pts = btn.querySelector('.points-badge');
          if (pts) pts.className = 'font-label-sm text-[12px] font-bold text-secondary points-badge shrink-0';
          const indicator = btn.querySelector('.status-indicator');
          if (indicator) indicator.className = 'status-indicator w-6 h-6 rounded-full bg-surface-container-high flex items-center justify-center transition-colors shrink-0';
          const icon = btn.querySelector('.check-icon');
          if (icon) {{
            icon.classList.remove('opacity-100', 'text-on-primary', 'text-on-tertiary', 'text-on-secondary');
            icon.classList.add('opacity-0', 'text-secondary');
          }}
        }});
      }}

      function applySelectionStyle(btn, type) {{
        const cfg = OPTION_STYLES[type];
        if (!cfg) return;
        btn.classList.remove('bg-surface-container-lowest', 'text-on-surface');
        btn.classList.add(cfg.bg, cfg.text, 'shadow-md');
        const sub = btn.querySelector('.sub-text');
        if (sub) {{
          sub.classList.remove('text-secondary');
          sub.classList.add(cfg.sub);
        }}
        const pts = btn.querySelector('.points-badge');
        if (pts) {{
          pts.classList.remove('text-secondary');
          pts.classList.add(cfg.sub);
        }}
        const indicator = btn.querySelector('.status-indicator');
        if (indicator) {{
          indicator.classList.remove('bg-surface-container-high');
          indicator.classList.add(cfg.indicatorBg);
        }}
        const icon = btn.querySelector('.check-icon');
        if (icon) {{
          icon.classList.remove('opacity-0', 'text-secondary');
          icon.classList.add('opacity-100', cfg.indicatorText);
        }}
      }}

      function renderCurrentQuestion() {{
        const total = activeQuestions.length;
        const currentQ = activeQuestions[currentIndex];
        const stepNum = currentIndex + 1;
        const pct = Math.round((stepNum / total) * 100);

        diagQBadge.textContent = `設問 ${{stepNum}}`;
        diagCurrentNum.textContent = stepNum;
        diagTotalNum.textContent = `/ ${{total}} 完了`;
        diagProgressPct.textContent = `${{pct}}%`;
        diagProgressFill.style.width = `${{pct}}%`;

        diagCategoryBadge.textContent = currentQ.categories.length > 0 
          ? currentQ.categories.join('・') 
          : '総合評価';

        diagQIndexLabel.textContent = `Q.${{currentQ.id}}`;
        diagQuestionText.textContent = `「${{currentQ.text}}」`;

        // If previously answered
        resetOptionButtons();
        const prevAnswer = userAnswers[currentQ.id];
        if (prevAnswer) {{
          const matchingBtn = Array.from(optionButtons).find(b => b.getAttribute('data-val') === prevAnswer);
          if (matchingBtn) applySelectionStyle(matchingBtn, prevAnswer);
        }}

        // Back button state
        if (currentIndex === 0) {{
          prevBtn.innerHTML = '<span class="material-symbols-outlined text-[18px]">home</span><span>最初の画面に戻る</span>';
        }} else {{
          prevBtn.innerHTML = '<span class="material-symbols-outlined text-[18px]">arrow_back</span><span>前の設問に戻る</span>';
        }}
      }}

      // Handle Option Selection
      let isTransitioning = false;
      optionButtons.forEach(btn => {{
        btn.addEventListener('click', () => {{
          if (isTransitioning) return;
          const val = btn.getAttribute('data-val');
          const currentQ = activeQuestions[currentIndex];

          resetOptionButtons();
          applySelectionStyle(btn, val);
          userAnswers[currentQ.id] = val;

          isTransitioning = true;
          setTimeout(() => {{
            isTransitioning = false;
            if (currentIndex < activeQuestions.length - 1) {{
              currentIndex++;
              renderCurrentQuestion();
            }} else {{
              showResults();
            }}
          }}, 240);
        }});
      }});

      // Handle Prev Button
      prevBtn.addEventListener('click', () => {{
        if (currentIndex > 0) {{
          currentIndex--;
          renderCurrentQuestion();
        }} else {{
          headerModeBadge.classList.add('hidden');
          showScreen(screenStart);
        }}
      }});

      // --- RESULTS CALCULATION & RENDERING (5-Point Likert Scale) ---
      const POINT_MAP = {{
        agree: 2,
        somewhat_agree: 1,
        neutral: 0,
        somewhat_disagree: -1,
        disagree: -2,
        // Legacy 3-choice fallback:
        yes: 2,
        no: -2
      }};

      function calculateScores() {{
        const total = activeQuestions.length;
        let totalPoints = 0;

        activeQuestions.forEach(q => {{
          const ans = userAnswers[q.id];
          const pt = POINT_MAP[ans] ?? 0;
          totalPoints += pt;
        }});

        // Normalized score from [-2N, +2N] to [0, 100]
        const maxPoints = 2 * total;
        const normalized = (totalPoints + maxPoints) / (2 * maxPoints);
        const overallLevel = Math.round(normalized * 100);

        // Parameters analysis: (-100% to +100%)
        const paramScores = {{}};
        CATEGORIES.forEach(cat => {{
          const catQuestions = activeQuestions.filter(q => q.categories.includes(cat));
          if (catQuestions.length === 0) {{
            paramScores[cat] = 0;
            return;
          }}
          let catPoints = 0;
          catQuestions.forEach(q => {{
            const ans = userAnswers[q.id];
            const pt = POINT_MAP[ans] ?? 0;
            catPoints += pt;
          }});
          const score = Math.round((catPoints / (2 * catQuestions.length)) * 100);
          paramScores[cat] = score;
        }});

        return {{ overallLevel, paramScores }};
      }}

      function showResults() {{
        headerModeBadge.classList.add('hidden');
        const {{ overallLevel, paramScores }} = calculateScores();

        resultUserName.textContent = `${{userName}} さんの診断結果`;

        // Classification & Verdict
        const isOtokomae = overallLevel >= 50;
        if (isOtokomae) {{
          verdictTag.className = 'inline-flex items-center px-3 py-1 rounded-full bg-primary text-on-primary font-label-md text-label-md tracking-wider shadow-sm';
          verdictTag.textContent = '男前';
          resultBadgeIcon.textContent = 'military_tech';
          verdictSummary.textContent = '行動基準がストイックかつ圧倒的な胆力と自己責任マインドを兼ね備えたタイプ。環境を言い訳にせず自己規律を貫徹する精神的自律性が極めて顕著です。';
        }} else {{
          verdictTag.className = 'inline-flex items-center px-3 py-1 rounded-full bg-secondary text-on-secondary font-label-md text-label-md tracking-wider shadow-sm';
          verdictTag.textContent = '女々しい';
          resultBadgeIcon.textContent = 'sentiment_calm';
          verdictSummary.textContent = '過酷な成果主義や理不尽な精神論よりも、情緒的共感や個人の自由度を大切にするタイプ。他者への配慮と柔軟性を重んじ、無理のない調和を求める傾向があります。';
        }}

        // Render Parameters Bars
        const sortedCats = [...CATEGORIES].sort((a, b) => paramScores[b] - paramScores[a]);

        parametersContainer.innerHTML = '';
        sortedCats.forEach(cat => {{
          const val = paramScores[cat];
          const isPos = val >= 0;
          const displayPct = isPos ? `+${{val}}%` : `${{val}}%`;
          const absVal = Math.min(Math.abs(val), 100);

          const barItem = document.createElement('div');
          barItem.className = 'space-y-1';

          let meterHtml = '';
          if (isPos) {{
            meterHtml = `
              <div class="relative h-2.5 w-full rounded-full bg-surface-container overflow-hidden flex">
                <div class="w-1/2 h-full flex justify-end relative">
                  <div class="absolute right-0 top-0 bottom-0 w-[1px] bg-outline-variant z-10"></div>
                </div>
                <div class="w-1/2 h-full flex justify-start relative">
                  <div class="h-full bg-primary-container rounded-r-full transition-all duration-700 ease-out" style="width: ${{absVal}}%;"></div>
                </div>
              </div>
            `;
          }} else {{
            meterHtml = `
              <div class="relative h-2.5 w-full rounded-full bg-surface-container overflow-hidden flex">
                <div class="w-1/2 h-full flex justify-end relative">
                  <div class="absolute right-0 top-0 bottom-0 w-[1px] bg-outline-variant z-10"></div>
                  <div class="h-full bg-secondary rounded-l-full transition-all duration-700 ease-out" style="width: ${{absVal}}%;"></div>
                </div>
                <div class="w-1/2 h-full flex justify-start relative"></div>
              </div>
            `;
          }}

          barItem.innerHTML = `
            <div class="flex justify-between items-center">
              <span class="font-label-md text-label-md text-on-surface font-medium">${{cat}}</span>
              <span class="font-label-md text-label-md ${{isPos ? 'text-primary font-semibold' : 'text-secondary font-semibold'}}">${{displayPct}}</span>
            </div>
            ${{meterHtml}}
          `;
          parametersContainer.appendChild(barItem);
        }});

        // Profile In-Depth Commentary
        const top1 = sortedCats[0];
        const top2 = sortedCats[1];
        const top1Val = paramScores[top1];
        const top2Val = paramScores[top2];

        if (isOtokomae) {{
          profileHeadline.textContent = 'コア・アドバンテージ';
          profileDescription.textContent = `${{top1}}（${{top1Val >= 0 ? '+' : ''}}${{top1Val}}%）と${{top2}}（${{top2Val >= 0 ? '+' : ''}}${{top2Val}}%）が群を抜いて高く、${{CATEGORY_DESCRIPTIONS[top1] || '強靭な自己規律'}}を軸に自身を鍛錬し続ける構造的タフネスを持っています。逆境下でも感情に流されず、客観的成果と精神的自律に準拠して最短で解を導き出します。`;
        }} else {{
          profileHeadline.textContent = 'コア・パーソナリティ';
          profileDescription.textContent = `組織の同調圧力や厳しい上下関係に対して一定の心理的距離を保ち、自己の感性やバランス感覚を尊重するプロファイルです。${{top1}}（${{top1Val >= 0 ? '+' : ''}}${{top1Val}}%）に見られるように、理不尽な要求に屈しない柔軟な思考と人間らしい共感力を兼ね備えています。`;
        }}

        // Save diagnosis log to Database (Firebase / LocalStorage)
        const answerPoints = {{}};
        Object.entries(userAnswers).forEach(([qid, ans]) => {{
          answerPoints[qid] = POINT_MAP[ans] ?? 0;
        }});

        saveDiagnosisLog({{
          userName,
          mode: currentMode,
          version: 2,
          scale: 5,
          totalQuestions: activeQuestions.length,
          overallLevel,
          verdict: isOtokomae ? '男前' : '女々しい',
          paramScores,
          answers: userAnswers,
          answerPoints: answerPoints,
          userAgent: navigator.userAgent
        }});

        // Show screen
        showScreen(screenResult);

        // Circular Score Gauge Animation
        const targetOffset = 251.2 * (1 - (overallLevel / 100));
        scoreCircleBar.style.strokeDashoffset = '251.2';
        setTimeout(() => {{
          scoreCircleBar.style.strokeDashoffset = `${{targetOffset}}`;
        }}, 100);

        // Number Counter Animation
        let count = 0;
        const duration = 1000;
        const stepTime = 15;
        const totalSteps = duration / stepTime;
        const increment = overallLevel / totalSteps;
        const counterTimer = setInterval(() => {{
          count += increment;
          if (count >= overallLevel) {{
            count = overallLevel;
            clearInterval(counterTimer);
          }}
          scoreCounter.textContent = Math.round(count);
        }}, stepTime);
      }}

      // --- SHARE ACTION ---
      shareBtn.addEventListener('click', async () => {{
        const {{ overallLevel }} = calculateScores();
        const verdict = overallLevel >= 50 ? '男前' : '女々しい';
        const shareData = {{
          title: '大和男児か診断結果',
          text: `総合大和男児レベル${{overallLevel}}%【${{verdict}}】でした。 #大和男児か診断`,
          url: window.location.href
        }};

        if (navigator.share) {{
          try {{
            await navigator.share(shareData);
          }} catch (err) {{}}
        }} else {{
          try {{
            await navigator.clipboard.writeText(`${{shareData.text}} ${{window.location.href}}`);
            const originalContent = shareBtn.innerHTML;
            shareBtn.innerHTML = '<span class="material-symbols-outlined text-[18px]">check</span><span>クリップボードにコピーしました</span>';
            setTimeout(() => {{
              shareBtn.innerHTML = originalContent;
            }}, 2200);
          }} catch (e) {{}}
        }}
      }});

      // --- RETEST ACTION ---
      retestBtn.addEventListener('click', () => {{
        showScreen(screenStart);
      }});

      // Initial state update
      updateNameState();
    }})();
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Generated index.html successfully!")


# ==========================================
# 2. BUILD admin.html (Hidden Analytics Dashboard)
# ==========================================
admin_html = f'''<!DOCTYPE html>
<html lang="ja" class="h-full">
<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>大和男児か診断 - 分析ダッシュボード</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Firebase SDK (compat) -->
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore-compat.js"></script>
  <script src="firebase-config.js"></script>
  <script id="tailwind-config">
    tailwind.config = {{
      darkMode: "class",
      theme: {{
        extend: {{
          colors: {{
            "surface-tint": "#516071",
            "tertiary-container": "#433628",
            "surface-container-low": "#f2f4f6",
            "on-tertiary-fixed": "#241a0d",
            "secondary-fixed-dim": "#b7c8db",
            "on-secondary-fixed-variant": "#384858",
            "on-background": "#191c1e",
            "on-error-container": "#93000a",
            "surface-container-high": "#e7e8ea",
            "inverse-surface": "#2e3132",
            "on-primary-container": "#94a4b7",
            "tertiary": "#2c2114",
            "inverse-on-surface": "#f0f1f3",
            "on-primary-fixed-variant": "#394859",
            "on-tertiary-fixed-variant": "#524435",
            "on-secondary": "#ffffff",
            "surface-container-lowest": "#ffffff",
            "surface-container-highest": "#e1e2e4",
            "on-surface-variant": "#44474c",
            "on-tertiary-container": "#b19f8c",
            "inverse-primary": "#b8c8dc",
            "primary-container": "#2b3a4a",
            "surface-variant": "#e1e2e4",
            "surface-container": "#edeef0",
            "primary": "#152434",
            "surface": "#f8f9fb",
            "outline": "#74777c",
            "on-tertiary": "#ffffff",
            "primary-fixed-dim": "#b8c8dc",
            "surface-dim": "#d9dadc",
            "on-surface": "#191c1e",
            "secondary": "#4f6070",
            "tertiary-fixed": "#f4dfca",
            "error-container": "#ffdad6",
            "on-secondary-fixed": "#0b1d2b",
            "outline-variant": "#c4c6cc",
            "secondary-container": "#d3e4f8",
            "tertiary-fixed-dim": "#d7c3af",
            "secondary-fixed": "#d3e4f8",
            "primary-fixed": "#d4e4f9",
            "background": "#f8f9fb",
            "on-error": "#ffffff",
            "on-secondary-container": "#556677",
            "surface-bright": "#f8f9fb",
            "on-primary": "#ffffff",
            "error": "#ba1a1a",
            "on-primary-fixed": "#0d1d2c"
          }},
          borderRadius: {{
            "DEFAULT": "0.25rem",
            "lg": "0.5rem",
            "xl": "0.75rem",
            "full": "9999px"
          }},
          fontFamily: {{
            "headline-sm": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "body-sm": ["Noto Sans", "sans-serif"],
            "label-lg": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "headline-xl": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "headline-lg": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "headline-xl-mobile": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "label-md": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "headline-lg-mobile": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "label-sm": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"],
            "body-lg": ["Noto Sans", "sans-serif"],
            "body-md": ["Noto Sans", "sans-serif"],
            "headline-md": ["Plus Jakarta Sans", "Noto Sans", "sans-serif"]
          }}
        }}
      }}
    }};
  </script>
</head>
<body class="bg-surface font-body-md text-on-surface antialiased min-h-screen flex flex-col">

  <!-- Top Navigation Header -->
  <header class="sticky top-0 z-40 bg-surface/90 backdrop-blur-xl border-b border-surface-container shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <span class="material-symbols-outlined text-primary text-2xl">analytics</span>
        <div>
          <h1 class="font-headline-sm text-headline-sm text-primary font-bold tracking-tight">
            大和男児か診断 分析ダッシュボード
          </h1>
          <span class="text-[11px] text-secondary">全ユーザー回答・動向統合ログ</span>
        </div>
      </div>

      <!-- Header Actions -->
      <div class="flex items-center gap-2.5">
        <!-- Live Status Pill -->
        <div id="db-status-pill" class="flex items-center gap-1.5 px-3 py-1 rounded-full text-[12px] font-medium bg-amber-100 text-amber-800 border border-amber-300">
          <span class="w-2 h-2 rounded-full bg-amber-500 animate-pulse"></span>
          <span id="db-status-text">ローカル保存中</span>
        </div>

        <!-- Firebase Config Button -->
        <button id="open-config-btn" class="h-9 px-3 rounded-lg bg-surface-container hover:bg-surface-container-high text-on-surface text-[13px] font-medium flex items-center gap-1.5 transition-colors" type="button">
          <span class="material-symbols-outlined text-[18px] text-secondary">settings</span>
          <span class="hidden sm:inline">Firebase設定</span>
        </button>

        <!-- CSV Export Button -->
        <button id="export-csv-btn" class="h-9 px-3.5 rounded-lg bg-primary-container text-on-primary text-[13px] font-medium flex items-center gap-1.5 shadow-sm hover:opacity-95 active:scale-95 transition-all" type="button">
          <span class="material-symbols-outlined text-[18px]">download</span>
          <span>CSVエクスポート</span>
        </button>

        <!-- Back to Diagnosis Link -->
        <a href="index.html" class="h-9 px-3 rounded-lg bg-surface-container-lowest border border-outline-variant/40 hover:bg-surface-container text-secondary text-[13px] font-medium flex items-center gap-1 transition-colors" title="診断ページへ">
          <span class="material-symbols-outlined text-[18px]">open_in_new</span>
          <span class="hidden md:inline">診断画面</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Main Container -->
  <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">

    <!-- Firebase Connection Banner (shown if not configured) -->
    <div id="firebase-prompt-banner" class="rounded-xl p-4 bg-amber-50 border border-amber-200 text-amber-900 flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-sm">
      <div class="flex items-start gap-3">
        <span class="material-symbols-outlined text-amber-600 text-2xl mt-0.5">cloud_off</span>
        <div class="space-y-0.5">
          <p class="font-semibold text-[14px]">Firebase未接続（現在は端末内ローカルデータを表示中）</p>
          <p class="text-[12px] text-amber-700">無料のFirebase (Firestore) を連携すると、他人のスマホや全端末からの回答が自動でリアルタイム集計されます。</p>
        </div>
      </div>
      <button id="banner-config-btn" class="self-start sm:self-auto px-3.5 py-1.5 rounded-lg bg-amber-700 text-white font-medium text-[12px] hover:bg-amber-800 transition-colors shrink-0">
        1分で接続設定する
      </button>
    </div>

    <!-- KPI Summary Metrics (4 Cards) -->
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
      <!-- 1. Total Submissions -->
      <div class="bg-surface-container-lowest p-5 rounded-xl shadow-sm border border-outline-variant/20 flex flex-col justify-between">
        <span class="text-[12px] font-medium text-secondary">総診断数</span>
        <div class="mt-2 flex items-baseline gap-2">
          <span id="kpi-total" class="font-headline-xl text-3xl font-bold text-primary">0</span>
          <span class="text-[12px] text-secondary">件</span>
        </div>
        <span id="kpi-recent-time" class="text-[11px] text-outline mt-1 truncate">最終更新: なし</span>
      </div>

      <!-- 2. Avg Score -->
      <div class="bg-surface-container-lowest p-5 rounded-xl shadow-sm border border-outline-variant/20 flex flex-col justify-between">
        <span class="text-[12px] font-medium text-secondary">平均 大和男児レベル</span>
        <div class="mt-2 flex items-baseline gap-2">
          <span id="kpi-avg-score" class="font-headline-xl text-3xl font-bold text-primary">0</span>
          <span class="text-[12px] text-secondary">%</span>
        </div>
        <div class="w-full bg-surface-container h-1.5 rounded-full mt-2 overflow-hidden">
          <div id="kpi-avg-bar" class="h-full bg-primary-container rounded-full" style="width: 0%;"></div>
        </div>
      </div>

      <!-- 3. Verdict Distribution -->
      <div class="bg-surface-container-lowest p-5 rounded-xl shadow-sm border border-outline-variant/20 flex flex-col justify-between">
        <span class="text-[12px] font-medium text-secondary">判定分布</span>
        <div class="mt-1 flex items-center justify-between text-[13px]">
          <span class="text-primary font-semibold">男前: <span id="kpi-otokomae-count">0</span>件 (<span id="kpi-otokomae-pct">0</span>%)</span>
          <span class="text-secondary font-semibold">女々しい: <span id="kpi-memeshii-count">0</span>件</span>
        </div>
        <div class="w-full bg-surface-container h-2 rounded-full mt-2 overflow-hidden flex">
          <div id="kpi-otokomae-bar" class="h-full bg-primary" style="width: 0%;"></div>
          <div id="kpi-memeshii-bar" class="h-full bg-secondary" style="width: 100%;"></div>
        </div>
      </div>

      <!-- 4. Mode Ratio -->
      <div class="bg-surface-container-lowest p-5 rounded-xl shadow-sm border border-outline-variant/20 flex flex-col justify-between">
        <span class="text-[12px] font-medium text-secondary">診断モード比率</span>
        <div class="mt-1 flex items-center justify-between text-[13px]">
          <span class="text-primary font-semibold">フル: <span id="kpi-mode-full-count">0</span></span>
          <span class="text-secondary font-semibold">クイック: <span id="kpi-mode-quick-count">0</span></span>
        </div>
        <div class="w-full bg-surface-container h-2 rounded-full mt-2 overflow-hidden flex">
          <div id="kpi-mode-full-bar" class="h-full bg-primary-container" style="width: 0%;"></div>
          <div id="kpi-mode-quick-bar" class="h-full bg-surface-container-highest" style="width: 100%;"></div>
        </div>
      </div>
    </div>

    <!-- Parameter Population Averages (8 Dimensions) -->
    <div class="bg-surface-container-lowest p-6 rounded-xl shadow-sm border border-outline-variant/20 space-y-4">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
        <div class="flex items-center gap-2">
          <span class="material-symbols-outlined text-secondary text-[22px]">bar_chart</span>
          <h2 class="font-headline-sm text-headline-sm text-primary font-bold">全回答者 パラメーター平均値</h2>
        </div>
        <span class="text-[12px] text-secondary">中央0%基準（右: 肯定 / 左: 否定）</span>
      </div>

      <div id="global-param-meters" class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-3 pt-2">
        <!-- Rendered dynamically -->
      </div>
    </div>

    <!-- Submissions Table Card -->
    <div class="bg-surface-container-lowest rounded-xl shadow-sm border border-outline-variant/20 overflow-hidden space-y-4 p-5">
      <!-- Table Filter Bar -->
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-3 pb-3 border-b border-surface-container">
        <div class="flex items-center gap-2">
          <span class="material-symbols-outlined text-secondary text-[20px]">table_rows</span>
          <h3 class="font-headline-sm text-[16px] text-primary font-bold">回答ログ一覧</h3>
          <span id="filtered-count-badge" class="px-2 py-0.5 rounded-full text-[11px] bg-surface-container text-secondary font-medium">0件</span>
        </div>

        <div class="flex flex-wrap items-center gap-2.5">
          <!-- Search Input -->
          <div class="relative flex items-center">
            <span class="material-symbols-outlined absolute left-2.5 text-secondary text-[18px]">search</span>
            <input id="search-input" type="text" placeholder="名前を検索..." class="h-9 pl-8 pr-3 rounded-lg bg-surface-container-low text-[13px] text-primary placeholder:text-outline outline-none focus:ring-1 focus:ring-primary w-40 sm:w-56">
          </div>

          <!-- Verdict Filter -->
          <select id="verdict-filter" class="h-9 px-3 rounded-lg bg-surface-container-low text-[13px] text-primary outline-none">
            <option value="all">判定: すべて</option>
            <option value="男前">男前 のみ</option>
            <option value="女々しい">女々しい のみ</option>
          </select>

          <!-- Mode Filter -->
          <select id="mode-filter" class="h-9 px-3 rounded-lg bg-surface-container-low text-[13px] text-primary outline-none">
            <option value="all">モード: すべて</option>
            <option value="full">精密フル (85問)</option>
            <option value="quick">クイック (30問)</option>
          </select>

          <!-- Clear Data Button -->
          <button id="clear-local-btn" class="h-9 px-2.5 rounded-lg text-outline hover:text-error text-[12px] flex items-center gap-1 transition-colors" title="ローカルログを消去">
            <span class="material-symbols-outlined text-[16px]">delete</span>
            <span class="hidden lg:inline">クリア</span>
          </button>
        </div>
      </div>

      <!-- Table Container -->
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse text-[13px]">
          <thead>
            <tr class="border-b border-surface-container text-secondary font-medium">
              <th class="py-3 px-3">日時</th>
              <th class="py-3 px-3">お名前</th>
              <th class="py-3 px-3">モード</th>
              <th class="py-3 px-3">大和男児レベル</th>
              <th class="py-3 px-3">判定</th>
              <th class="py-3 px-3">突出パラメーター</th>
              <th class="py-3 px-3 text-right">操作</th>
            </tr>
          </thead>
          <tbody id="logs-tbody" class="divide-y divide-surface-container">
            <tr>
              <td colspan="7" class="py-8 text-center text-secondary">
                ログを読み込み中...
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </main>

  <!-- ========================================== -->
  <!-- MODAL 1: ANSWER DETAIL MODAL -->
  <!-- ========================================== -->
  <div id="detail-modal" class="fixed inset-0 z-50 hidden bg-black/40 backdrop-blur-sm flex items-center justify-center p-3 sm:p-6">
    <div class="bg-surface-container-lowest rounded-2xl shadow-xl w-full max-w-3xl max-h-[90vh] flex flex-col overflow-hidden border border-outline-variant/30 animate-in fade-in zoom-in-95 duration-200">
      <!-- Modal Header -->
      <div class="p-5 border-b border-surface-container flex items-center justify-between bg-surface-container-lowest">
        <div>
          <div class="flex items-center gap-2">
            <h3 id="modal-user-name" class="font-headline-sm text-lg font-bold text-primary">ユーザー名</h3>
            <span id="modal-verdict-badge" class="px-2.5 py-0.5 rounded-full text-[12px] font-semibold bg-primary text-white">男前</span>
          </div>
          <span id="modal-meta-info" class="text-[12px] text-secondary">2026/11/02 23:00 ・ フル診断 (85問) ・ レベル 78%</span>
        </div>
        <button id="close-modal-btn" class="p-1.5 rounded-full text-secondary hover:text-primary hover:bg-surface-container transition-colors">
          <span class="material-symbols-outlined text-2xl">close</span>
        </button>
      </div>

      <!-- Modal Body (Scrollable) -->
      <div class="p-5 overflow-y-auto space-y-6 flex-1 bg-surface">
        <!-- User Parameters Summary -->
        <div class="bg-surface-container-lowest p-4 rounded-xl border border-surface-container space-y-3">
          <h4 class="text-[13px] font-bold text-primary flex items-center gap-1.5">
            <span class="material-symbols-outlined text-[18px] text-secondary">insights</span>
            <span>パラメーター獲得スコア</span>
          </h4>
          <div id="modal-param-chips" class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-[12px]"></div>
        </div>

        <!-- All Questions Breakdown -->
        <div class="space-y-3">
          <h4 class="text-[13px] font-bold text-primary flex items-center gap-1.5">
            <span class="material-symbols-outlined text-[18px] text-secondary">fact_check</span>
            <span>全問の回答詳細</span>
          </h4>
          <div id="modal-answers-list" class="space-y-2">
            <!-- Rendered dynamically -->
          </div>
        </div>
      </div>

      <!-- Modal Footer -->
      <div class="p-4 border-t border-surface-container bg-surface-container-lowest flex justify-end">
        <button id="modal-close-action-btn" class="px-4 py-2 rounded-lg bg-surface-container text-on-surface font-medium text-[13px] hover:bg-surface-container-high transition-colors">
          閉じる
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- MODAL 2: FIREBASE SETTINGS MODAL -->
  <!-- ========================================== -->
  <div id="config-modal" class="fixed inset-0 z-50 hidden bg-black/40 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-surface-container-lowest rounded-2xl shadow-xl w-full max-w-xl max-h-[90vh] flex flex-col overflow-hidden border border-outline-variant/30">
      <div class="p-5 border-b border-surface-container flex items-center justify-between">
        <div class="flex items-center gap-2">
          <span class="material-symbols-outlined text-primary text-xl">settings</span>
          <h3 class="font-headline-sm text-base font-bold text-primary">Firebase接続設定</h3>
        </div>
        <button id="close-config-modal-btn" class="p-1 rounded-full text-secondary hover:text-primary transition-colors">
          <span class="material-symbols-outlined text-2xl">close</span>
        </button>
      </div>

      <div class="p-5 overflow-y-auto space-y-4 text-[13px]">
        <div class="p-3.5 rounded-lg bg-surface-container-low text-on-surface space-y-1.5">
          <p class="font-semibold text-primary">💡 設定手順（所要時間：約2分・無料）</p>
          <ol class="list-decimal list-inside space-y-1 text-secondary text-[12px]">
            <li><a href="https://console.firebase.google.com/" target="_blank" class="text-blue-600 underline font-medium">Firebase Console</a> でプロジェクトを無料作成</li>
            <li>メニューの「Firestore Database」を作成（「テストモードで開始」を選択）</li>
            <li>「プロジェクト設定」→「ウェブアプリを追加」し、表示された <code class="bg-surface-container px-1 py-0.5 rounded font-mono">firebaseConfig</code> をコピーして下枠に貼り付けてください。</li>
          </ol>
        </div>

        <div class="space-y-1.5">
          <label class="font-medium text-primary flex items-center justify-between" for="config-paste-area">
            <span>firebaseConfig を貼り付け</span>
            <span class="text-[11px] text-secondary">JSONまたはコードスニペット対応</span>
          </label>
          <textarea id="config-paste-area" rows="8" placeholder='const firebaseConfig = {{
  apiKey: "AIzaSy...",
  authDomain: "your-app.firebaseapp.com",
  projectId: "your-app",
  storageBucket: "your-app.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:12345:web:abcdef"
}};' class="w-full p-3 rounded-lg font-mono text-[11px] bg-surface-container-low text-primary border border-outline-variant/40 outline-none focus:ring-1 focus:ring-primary"></textarea>
        </div>

        <div id="config-feedback" class="hidden text-[12px] p-2.5 rounded-lg"></div>
      </div>

      <div class="p-4 border-t border-surface-container bg-surface-container-lowest flex items-center justify-between">
        <button id="reset-config-btn" class="text-secondary hover:text-error text-[12px] font-medium transition-colors">
          設定をリセット
        </button>
        <div class="flex items-center gap-2">
          <button id="cancel-config-btn" class="px-3.5 py-2 rounded-lg bg-surface-container text-secondary text-[13px] font-medium hover:bg-surface-container-high">
            キャンセル
          </button>
          <button id="save-config-btn" class="px-4 py-2 rounded-lg bg-primary text-on-primary text-[13px] font-medium shadow-sm hover:opacity-95">
            保存して接続
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Dashboard Script -->
  <script>
    (function() {{
      const ALL_QUESTIONS = {questions_json_str};
      const CATEGORIES = [
        'ストイシズム',
        '自己責任論',
        'メリトクラシー',
        '体育会的権威主義',
        'マッチョイズム',
        'ルッキズム',
        '優生思想',
        'ナショナリズム'
      ];

      // --- STATE ---
      let allLogs = [];
      let firestoreDb = null;
      let unsubscribeFirestore = null;

      // --- DOM REFS ---
      const dbStatusPill = document.getElementById('db-status-pill');
      const dbStatusText = document.getElementById('db-status-text');
      const firebasePromptBanner = document.getElementById('firebase-prompt-banner');
      const bannerConfigBtn = document.getElementById('banner-config-btn');
      const openConfigBtn = document.getElementById('open-config-btn');

      const kpiTotal = document.getElementById('kpi-total');
      const kpiRecentTime = document.getElementById('kpi-recent-time');
      const kpiAvgScore = document.getElementById('kpi-avg-score');
      const kpiAvgBar = document.getElementById('kpi-avg-bar');
      const kpiOtokomaeCount = document.getElementById('kpi-otokomae-count');
      const kpiOtokomaePct = document.getElementById('kpi-otokomae-pct');
      const kpiMemeshiiCount = document.getElementById('kpi-memeshii-count');
      const kpiOtokomaeBar = document.getElementById('kpi-otokomae-bar');
      const kpiMemeshiiBar = document.getElementById('kpi-memeshii-bar');
      const kpiModeFullCount = document.getElementById('kpi-mode-full-count');
      const kpiModeQuickCount = document.getElementById('kpi-mode-quick-count');
      const kpiModeFullBar = document.getElementById('kpi-mode-full-bar');
      const kpiModeQuickBar = document.getElementById('kpi-mode-quick-bar');

      const globalParamMeters = document.getElementById('global-param-meters');
      const logsTbody = document.getElementById('logs-tbody');
      const filteredCountBadge = document.getElementById('filtered-count-badge');
      const searchInput = document.getElementById('search-input');
      const verdictFilter = document.getElementById('verdict-filter');
      const modeFilter = document.getElementById('mode-filter');
      const clearLocalBtn = document.getElementById('clear-local-btn');
      const exportCsvBtn = document.getElementById('export-csv-btn');

      // Modals
      const detailModal = document.getElementById('detail-modal');
      const closeModalBtn = document.getElementById('close-modal-btn');
      const modalCloseActionBtn = document.getElementById('modal-close-action-btn');
      const modalUserName = document.getElementById('modal-user-name');
      const modalVerdictBadge = document.getElementById('modal-verdict-badge');
      const modalMetaInfo = document.getElementById('modal-meta-info');
      const modalParamChips = document.getElementById('modal-param-chips');
      const modalAnswersList = document.getElementById('modal-answers-list');

      const configModal = document.getElementById('config-modal');
      const closeConfigModalBtn = document.getElementById('close-config-modal-btn');
      const cancelConfigBtn = document.getElementById('cancel-config-btn');
      const saveConfigBtn = document.getElementById('save-config-btn');
      const resetConfigBtn = document.getElementById('reset-config-btn');
      const configPasteArea = document.getElementById('config-paste-area');
      const configFeedback = document.getElementById('config-feedback');

      // --- FIREBASE HELPER ---
      function getStoredFirebaseConfig() {{
        try {{
          const saved = localStorage.getItem('imai_firebase_config');
          if (saved) return JSON.parse(saved);
        }} catch (e) {{}}
        if (window.FIREBASE_CONFIG && window.FIREBASE_CONFIG.projectId) {{
          return window.FIREBASE_CONFIG;
        }}
        return null;
      }}

      function initFirebaseConnection() {{
        const cfg = getStoredFirebaseConfig();
        if (cfg && cfg.projectId && typeof firebase !== 'undefined') {{
          try {{
            if (!firebase.apps.length) {{
              firebase.initializeApp(cfg);
            }}
            firestoreDb = firebase.firestore();

            // Set Pill to Online
            dbStatusPill.className = 'flex items-center gap-1.5 px-3 py-1 rounded-full text-[12px] font-medium bg-emerald-100 text-emerald-800 border border-emerald-300';
            dbStatusPill.innerHTML = '<span class="w-2 h-2 rounded-full bg-emerald-500"></span><span>Firestore クラウド同期中</span>';
            firebasePromptBanner.classList.add('hidden');

            // Listen to real-time changes
            if (unsubscribeFirestore) unsubscribeFirestore();

            function handleSnapshot(snapshot) {{
              const cloudLogs = [];
              snapshot.forEach(doc => {{
                cloudLogs.push({{ id: doc.id, ...doc.data() }});
              }});
              // Sort newest first
              cloudLogs.sort((a, b) => {{
                const timeA = a.createdAtStr ? new Date(a.createdAtStr).getTime() : 0;
                const timeB = b.createdAtStr ? new Date(b.createdAtStr).getTime() : 0;
                return timeB - timeA;
              }});
              allLogs = cloudLogs;
              renderDashboard();
            }}

            function handleFirestoreError(err) {{
              console.error('Firestore listener error:', err);
              dbStatusPill.className = 'flex items-center gap-1.5 px-3 py-1 rounded-full text-[12px] font-medium bg-red-100 text-red-800 border border-red-300';
              dbStatusPill.innerHTML = '<span class="w-2 h-2 rounded-full bg-red-500"></span><span>Firestore未作成または権限エラー</span>';

              firebasePromptBanner.classList.remove('hidden');
              firebasePromptBanner.className = 'rounded-xl p-4 bg-red-50 border border-red-200 text-red-900 flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-sm';
              firebasePromptBanner.innerHTML = `
                <div class="flex items-start gap-3">
                  <span class="material-symbols-outlined text-red-600 text-2xl mt-0.5">warning</span>
                  <div class="space-y-0.5">
                    <p class="font-semibold text-[14px]">Cloud Firestore データベースの作成が必要です</p>
                    <p class="text-[12px] text-red-700">Firebase Consoleの左メニュー「Firestore Database」から「データベースの作成（テストモードで開始）」を行ってください。</p>
                  </div>
                </div>
                <a href="https://console.firebase.google.com/project/${{cfg.projectId}}/firestore" target="_blank" class="self-start sm:self-auto px-3.5 py-1.5 rounded-lg bg-red-700 text-white font-medium text-[12px] hover:bg-red-800 transition-colors shrink-0">
                  Firestoreを作成する
                </a>
              `;
              loadLocalLogsFallback();
            }}

            const col = firestoreDb.collection('diagnoses');
            try {{
              unsubscribeFirestore = col.orderBy('createdAt', 'desc').onSnapshot(
                handleSnapshot,
                () => {{
                  unsubscribeFirestore = col.onSnapshot(handleSnapshot, handleFirestoreError);
                }}
              );
            }} catch (e) {{
              unsubscribeFirestore = col.onSnapshot(handleSnapshot, handleFirestoreError);
            }}

            return true;
          }} catch (e) {{
            console.error('Firebase setup failed:', e);
            loadLocalLogsFallback();
            return false;
          }}
        }} else {{
          loadLocalLogsFallback();
          return false;
        }}
      }}

      function loadLocalLogsFallback() {{
        dbStatusPill.className = 'flex items-center gap-1.5 px-3 py-1 rounded-full text-[12px] font-medium bg-amber-100 text-amber-800 border border-amber-300';
        dbStatusPill.innerHTML = '<span class="w-2 h-2 rounded-full bg-amber-500 animate-pulse"></span><span>ローカル保存中</span>';
        firebasePromptBanner.classList.remove('hidden');

        try {{
          allLogs = JSON.parse(localStorage.getItem('imai_diagnoses_log') || '[]');
        }} catch (e) {{
          allLogs = [];
        }}
        renderDashboard();
      }}

      // --- RENDER DASHBOARD ---
      function renderDashboard() {{
        const total = allLogs.length;
        kpiTotal.textContent = total;

        if (total === 0) {{
          kpiRecentTime.textContent = '最終更新: なし';
          kpiAvgScore.textContent = '0';
          kpiAvgBar.style.width = '0%';
          kpiOtokomaeCount.textContent = '0';
          kpiOtokomaePct.textContent = '0';
          kpiMemeshiiCount.textContent = '0';
          kpiOtokomaeBar.style.width = '0%';
          kpiMemeshiiBar.style.width = '100%';
          kpiModeFullCount.textContent = '0';
          kpiModeQuickCount.textContent = '0';
          renderGlobalParams({{}});
          renderTable([]);
          return;
        }}

        // Recent date
        const first = allLogs[0];
        if (first.createdAtStr) {{
          const d = new Date(first.createdAtStr);
          kpiRecentTime.textContent = `最新: ${{d.getMonth()+1}}/${{d.getDate()}} ${{String(d.getHours()).padStart(2, '0')}}:${{String(d.getMinutes()).padStart(2, '0')}}`;
        }}

        // Avg Score
        const sumScores = allLogs.reduce((acc, cur) => acc + (cur.overallLevel || 0), 0);
        const avgScore = Math.round(sumScores / total);
        kpiAvgScore.textContent = avgScore;
        kpiAvgBar.style.width = `${{avgScore}}%`;

        // Verdict distribution
        const otokomaeCount = allLogs.filter(l => l.verdict === '男前' || (l.overallLevel >= 50)).length;
        const memeshiiCount = total - otokomaeCount;
        const otokomaePct = Math.round((otokomaeCount / total) * 100);
        kpiOtokomaeCount.textContent = otokomaeCount;
        kpiOtokomaePct.textContent = otokomaePct;
        kpiMemeshiiCount.textContent = memeshiiCount;
        kpiOtokomaeBar.style.width = `${{otokomaePct}}%`;
        kpiMemeshiiBar.style.width = `${{100 - otokomaePct}}%`;

        // Mode ratio
        const fullCount = allLogs.filter(l => l.mode === 'full').length;
        const quickCount = total - fullCount;
        kpiModeFullCount.textContent = fullCount;
        kpiModeQuickCount.textContent = quickCount;
        const fullPct = Math.round((fullCount / total) * 100);
        kpiModeFullBar.style.width = `${{fullPct}}%`;
        kpiModeQuickBar.style.width = `${{100 - fullPct}}%`;

        // Calculate average parameters across all users
        const avgParams = {{}};
        CATEGORIES.forEach(cat => {{
          let sum = 0;
          let count = 0;
          allLogs.forEach(l => {{
            if (l.paramScores && typeof l.paramScores[cat] === 'number') {{
              sum += l.paramScores[cat];
              count++;
            }}
          }});
          avgParams[cat] = count > 0 ? Math.round(sum / count) : 0;
        }});
        renderGlobalParams(avgParams);

        // Filter and render table
        applyFilters();
      }}

      function renderGlobalParams(avgParams) {{
        globalParamMeters.innerHTML = '';
        CATEGORIES.forEach(cat => {{
          const val = avgParams[cat] || 0;
          const isPos = val >= 0;
          const absVal = Math.min(Math.abs(val), 100);
          const displayPct = isPos ? `+${{val}}%` : `${{val}}%`;

          const row = document.createElement('div');
          row.className = 'space-y-1';

          let barHtml = '';
          if (isPos) {{
            barHtml = `
              <div class="relative h-2 w-full rounded-full bg-surface-container overflow-hidden flex">
                <div class="w-1/2 h-full flex justify-end relative">
                  <div class="absolute right-0 top-0 bottom-0 w-[1px] bg-outline-variant z-10"></div>
                </div>
                <div class="w-1/2 h-full flex justify-start relative">
                  <div class="h-full bg-primary-container rounded-r-full" style="width: ${{absVal}}%;"></div>
                </div>
              </div>
            `;
          }} else {{
            barHtml = `
              <div class="relative h-2 w-full rounded-full bg-surface-container overflow-hidden flex">
                <div class="w-1/2 h-full flex justify-end relative">
                  <div class="absolute right-0 top-0 bottom-0 w-[1px] bg-outline-variant z-10"></div>
                  <div class="h-full bg-secondary rounded-l-full" style="width: ${{absVal}}%;"></div>
                </div>
                <div class="w-1/2 h-full flex justify-start relative"></div>
              </div>
            `;
          }}

          row.innerHTML = `
            <div class="flex justify-between items-center text-[12px]">
              <span class="font-medium text-on-surface">${{cat}}</span>
              <span class="font-semibold ${{isPos ? 'text-primary' : 'text-secondary'}}">${{displayPct}}</span>
            </div>
            ${{barHtml}}
          `;
          globalParamMeters.appendChild(row);
        }});
      }}

      function applyFilters() {{
        const search = searchInput.value.trim().toLowerCase();
        const verdict = verdictFilter.value;
        const mode = modeFilter.value;

        const filtered = allLogs.filter(l => {{
          if (search && !(l.userName || '').toLowerCase().includes(search)) return false;
          if (verdict !== 'all' && l.verdict !== verdict) return false;
          if (mode !== 'all' && l.mode !== mode) return false;
          return true;
        }});

        filteredCountBadge.textContent = `${{filtered.length}}件`;
        renderTable(filtered);
      }}

      searchInput.addEventListener('input', applyFilters);
      verdictFilter.addEventListener('change', applyFilters);
      modeFilter.addEventListener('change', applyFilters);

      function renderTable(logs) {{
        logsTbody.innerHTML = '';
        if (logs.length === 0) {{
          logsTbody.innerHTML = `
            <tr>
              <td colspan="7" class="py-8 text-center text-secondary">
                該当する診断ログがありません
              </td>
            </tr>
          `;
          return;
        }}

        logs.forEach(log => {{
          const tr = document.createElement('tr');
          tr.className = 'hover:bg-surface-container-low transition-colors';

          // Format Date
          let dateStr = '---';
          if (log.createdAtStr) {{
            const d = new Date(log.createdAtStr);
            dateStr = `${{d.getMonth()+1}}/${{d.getDate()}} ${{String(d.getHours()).padStart(2, '0')}}:${{String(d.getMinutes()).padStart(2, '0')}}`;
          }}

          // Verdict badge
          const isOtokomae = log.verdict === '男前' || (log.overallLevel >= 50);
          const verdictBadge = isOtokomae
            ? '<span class="inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-semibold bg-primary text-white">男前</span>'
            : '<span class="inline-flex items-center px-2 py-0.5 rounded-full text-[11px] font-semibold bg-secondary text-white">女々しい</span>';

          // Mode badge & Scale badge
          const scaleBadge = (log.scale === 5 || log.version === 2)
            ? '<span class="ml-1 px-1.5 py-0.2 rounded text-[10px] bg-emerald-50 text-emerald-700 border border-emerald-200">5択</span>'
            : '<span class="ml-1 px-1.5 py-0.2 rounded text-[10px] bg-surface-container text-secondary">3択</span>';
          const modeBadge = log.mode === 'quick'
            ? `<span class="px-1.5 py-0.5 rounded text-[11px] bg-surface-container text-secondary">クイック(30問)${{scaleBadge}}</span>`
            : `<span class="px-1.5 py-0.5 rounded text-[11px] bg-primary-fixed text-on-primary-fixed font-medium">精密フル(85問)${{scaleBadge}}</span>`;

          // Top traits
          let topTraitsStr = '---';
          if (log.paramScores) {{
            const sorted = Object.entries(log.paramScores).sort((a, b) => b[1] - a[1]);
            if (sorted.length >= 2) {{
              topTraitsStr = `${{sorted[0][0]}} (${{sorted[0][1] >= 0 ? '+' : ''}}${{sorted[0][1]}}%), ${{sorted[1][0]}} (${{sorted[1][1] >= 0 ? '+' : ''}}${{sorted[1][1]}}%)`;
            }}
          }}

          tr.innerHTML = `
            <td class="py-3 px-3 text-secondary text-[12px] whitespace-nowrap">${{dateStr}}</td>
            <td class="py-3 px-3 font-semibold text-primary truncate max-w-[120px]">${{log.userName || 'もにん'}}</td>
            <td class="py-3 px-3 whitespace-nowrap">${{modeBadge}}</td>
            <td class="py-3 px-3 font-bold text-primary">${{log.overallLevel ?? 0}}%</td>
            <td class="py-3 px-3 whitespace-nowrap">${{verdictBadge}}</td>
            <td class="py-3 px-3 text-secondary text-[12px] truncate max-w-[200px]">${{topTraitsStr}}</td>
            <td class="py-3 px-3 text-right whitespace-nowrap">
              <button class="view-detail-btn px-2.5 py-1 rounded bg-surface-container hover:bg-surface-container-high text-primary font-medium text-[12px] transition-colors" data-id="${{log.id}}">
                回答詳細
              </button>
            </td>
          `;

          tr.querySelector('.view-detail-btn').addEventListener('click', () => {{
            openDetailModal(log);
          }});

          logsTbody.appendChild(tr);
        }});
      }}

      // --- DETAIL MODAL ---
      function openDetailModal(log) {{
        modalUserName.textContent = `${{log.userName || 'もにん'}} さんの回答`;
        const isOtokomae = log.verdict === '男前' || (log.overallLevel >= 50);
        modalVerdictBadge.className = isOtokomae
          ? 'px-2.5 py-0.5 rounded-full text-[12px] font-semibold bg-primary text-white'
          : 'px-2.5 py-0.5 rounded-full text-[12px] font-semibold bg-secondary text-white';
        modalVerdictBadge.textContent = isOtokomae ? '男前' : '女々しい';

        const dStr = log.createdAtStr ? new Date(log.createdAtStr).toLocaleString('ja-JP') : '---';
        const modeText = log.mode === 'quick' ? 'クイック診断 (全30問)' : '精密フル診断 (全85問)';
        modalMetaInfo.textContent = `${{dStr}} ・ ${{modeText}} ・ 大和男児レベル ${{log.overallLevel ?? 0}}%`;

        // Param Chips
        modalParamChips.innerHTML = '';
        if (log.paramScores) {{
          Object.entries(log.paramScores).forEach(([cat, val]) => {{
            const isPos = val >= 0;
            const chip = document.createElement('div');
            chip.className = 'p-2 rounded-lg bg-surface-container flex items-center justify-between';
            chip.innerHTML = `
              <span class="text-secondary truncate">${{cat}}</span>
              <span class="font-bold ${{isPos ? 'text-primary' : 'text-secondary'}}">${{isPos ? '+' : ''}}${{val}}%</span>
            `;
            modalParamChips.appendChild(chip);
          }});
        }}

        // Questions List
        modalAnswersList.innerHTML = '';
        const userAnswers = log.answers || {{}};

        ALL_QUESTIONS.forEach(q => {{
          const isRelevantToMode = log.mode === 'full' || q.isFast;
          const ans = userAnswers[q.id];

          const item = document.createElement('div');
          item.className = 'p-3 rounded-lg bg-surface-container-lowest border border-surface-container flex items-start justify-between gap-3';

          let ansBadge = '';
          if (!isRelevantToMode && !ans) {{
            ansBadge = '<span class="px-2 py-0.5 rounded text-[11px] bg-surface-container text-outline whitespace-nowrap">モード対象外</span>';
          }} else if (ans === 'yes') {{
            ansBadge = '<span class="px-2.5 py-1 rounded-md text-[11px] font-semibold bg-primary text-white whitespace-nowrap flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">check</span>はい</span>';
          }} else if (ans === 'neutral') {{
            ansBadge = '<span class="px-2.5 py-1 rounded-md text-[11px] font-semibold bg-tertiary-container text-on-tertiary whitespace-nowrap flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">remove</span>中立</span>';
          }} else if (ans === 'no') {{
            ansBadge = '<span class="px-2.5 py-1 rounded-md text-[11px] font-semibold bg-secondary text-white whitespace-nowrap flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">close</span>いいえ</span>';
          }} else {{
            ansBadge = '<span class="px-2 py-0.5 rounded text-[11px] bg-surface-container text-outline whitespace-nowrap">未回答</span>';
          }}

          item.innerHTML = `
            <div class="space-y-1 flex-1">
              <div class="flex items-center gap-2">
                <span class="font-bold text-[12px] text-secondary">Q.${{q.id}}</span>
                <span class="text-[11px] px-1.5 py-0.2 rounded bg-surface-container text-secondary">${{q.categories.join('・')}}</span>
              </div>
              <p class="text-[13px] text-on-surface leading-snug">「${{q.text}}」</p>
            </div>
            <div class="shrink-0 pt-1">${{ansBadge}}</div>
          `;
          modalAnswersList.appendChild(item);
        }});

        detailModal.classList.remove('hidden');
      }}

      function closeDetailModal() {{
        detailModal.classList.add('hidden');
      }}
      closeModalBtn.addEventListener('click', closeDetailModal);
      modalCloseActionBtn.addEventListener('click', closeDetailModal);
      detailModal.addEventListener('click', (e) => {{
        if (e.target === detailModal) closeDetailModal();
      }});

      // --- CONFIG MODAL ---
      function openConfigModal() {{
        const stored = getStoredFirebaseConfig();
        if (stored) {{
          configPasteArea.value = JSON.stringify(stored, null, 2);
        }} else {{
          configPasteArea.value = '';
        }}
        configFeedback.classList.add('hidden');
        configModal.classList.remove('hidden');
      }}

      function closeConfigModal() {{
        configModal.classList.add('hidden');
      }}

      openConfigBtn.addEventListener('click', openConfigModal);
      bannerConfigBtn.addEventListener('click', openConfigModal);
      closeConfigModalBtn.addEventListener('click', closeConfigModal);
      cancelConfigBtn.addEventListener('click', closeConfigModal);
      configModal.addEventListener('click', (e) => {{
        if (e.target === configModal) closeConfigModal();
      }});

      // Parse and save Firebase Config
      saveConfigBtn.addEventListener('click', () => {{
        const raw = configPasteArea.value.trim();
        if (!raw) return;

        let parsedConfig = null;

        // Try direct JSON
        try {{
          parsedConfig = JSON.parse(raw);
        }} catch (e) {{
          // Try regex extraction from JS code snippet
          try {{
            const extract = (key) => {{
              const match = raw.match(new RegExp(`['"]?${{key}}['"]?\\s*:\\s*['"]([^'"]+)['"]`));
              return match ? match[1] : '';
            }};
            parsedConfig = {{
              apiKey: extract('apiKey'),
              authDomain: extract('authDomain'),
              projectId: extract('projectId'),
              storageBucket: extract('storageBucket'),
              messagingSenderId: extract('messagingSenderId'),
              appId: extract('appId')
            }};
          }} catch (err) {{}}
        }}

        if (!parsedConfig || !parsedConfig.projectId) {{
          configFeedback.className = 'text-[12px] p-2.5 rounded-lg bg-red-100 text-red-800 border border-red-200';
          configFeedback.textContent = 'エラー: projectId または apiKey が検出できませんでした。firebaseConfig をそのままコピー＆ペーストしてください。';
          configFeedback.classList.remove('hidden');
          return;
        }}

        localStorage.setItem('imai_firebase_config', JSON.stringify(parsedConfig));
        configFeedback.className = 'text-[12px] p-2.5 rounded-lg bg-emerald-100 text-emerald-800 border border-emerald-200';
        configFeedback.textContent = 'Firebase設定を保存しました！接続を初期化中...';
        configFeedback.classList.remove('hidden');

        setTimeout(() => {{
          closeConfigModal();
          initFirebaseConnection();
        }}, 600);
      }});

      resetConfigBtn.addEventListener('click', () => {{
        if (confirm('Firebase設定をリセットしてローカルモードに戻しますか？')) {{
          localStorage.removeItem('imai_firebase_config');
          configPasteArea.value = '';
          closeConfigModal();
          initFirebaseConnection();
        }}
      }});

      // --- CLEAR LOCAL LOGS ---
      clearLocalBtn.addEventListener('click', () => {{
        if (confirm('ローカル端末に保存されている診断ログを消去しますか？（Firebase上のデータは消去されません）')) {{
          localStorage.removeItem('imai_diagnoses_log');
          if (!firestoreDb) {{
            allLogs = [];
            renderDashboard();
          }}
        }}
      }});

      // --- CSV EXPORT (UTF-8 BOM for Excel) ---
      exportCsvBtn.addEventListener('click', () => {{
        if (allLogs.length === 0) {{
          alert('エクスポートするデータがありません。');
          return;
        }}

        // CSV Header
        const headers = [
          'ID',
          '診断日時',
          'お名前',
          '診断モード',
          '大和男児レベル(%)',
          '判定区分',
          ...CATEGORIES.map(c => `${{c}}(%)`),
          ...ALL_QUESTIONS.map(q => `Q${{q.id}}_${{q.text.replace(/[",]/g, '')}}`)
        ];

        const rows = allLogs.map(l => {{
          const dateStr = l.createdAtStr ? new Date(l.createdAtStr).toLocaleString('ja-JP') : '';
          const paramVals = CATEGORIES.map(c => l.paramScores ? (l.paramScores[c] ?? '') : '');
          const qVals = ALL_QUESTIONS.map(q => {{
            const ans = l.answers ? l.answers[q.id] : '';
            if (ans === 'agree') return '同意(+2)';
            if (ans === 'somewhat_agree') return 'やや同意(+1)';
            if (ans === 'neutral') return '中立(0)';
            if (ans === 'somewhat_disagree') return 'やや反対(-1)';
            if (ans === 'disagree') return '反対(-2)';
            if (ans === 'yes') return 'はい(+2)';
            if (ans === 'no') return 'いいえ(-2)';
            return '';
          }});

          return [
            `"${{l.id || ''}}"`,
            `"${{dateStr}}"`,
            `"${{(l.userName || 'もにん').replace(/"/g, '""')}}"`,
            `"${{l.mode === 'quick' ? 'クイック(30問)' : '精密フル(85問)'}}"`,
            l.overallLevel ?? '',
            `"${{l.verdict || ''}}"`,
            ...paramVals,
            ...qVals.map(v => `"${{v}}"`)
          ].join(',');
        }});

        const csvContent = '\\uFEFF' + [headers.join(','), ...rows].join('\\n');
        const blob = new Blob([csvContent], {{ type: 'text/csv;charset=utf-8;' }});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        const now = new Date();
        const dateStamp = now.toISOString().slice(0, 10).replace(/-/g, '') + '_' + String(now.getHours()).padStart(2, '0') + String(now.getMinutes()).padStart(2, '0');
        a.href = url;
        a.download = `yamato_shindan_analytics_${{dateStamp}}.csv`;
        a.click();
        URL.revokeObjectURL(url);
      }});

      // --- INITIALIZE ---
      initFirebaseConnection();
    }})();
  </script>
</body>
</html>
'''

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_html)

print("Generated admin.html successfully!")

