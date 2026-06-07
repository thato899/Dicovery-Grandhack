<html>
<body>
<!--StartFragment--><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">markdown</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span><span class="token title important" style="color: rgb(228, 86, 73);"><span class="token punctuation" style="color: rgb(56, 58, 66);">#</span> Setup &amp; Installation Guide</span></span>
<span></span>
<span><span class="token title important" style="color: rgb(228, 86, 73);"><span class="token punctuation" style="color: rgb(56, 58, 66);">##</span> Who Is This Guide For?</span></span>
<span></span>
<span><span class="token table"><span class="token table-header-row"><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-header important" style="color: rgb(228, 86, 73);"> Role </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-header important" style="color: rgb(228, 86, 73);"> What You Need From This Guide </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span></span></span>
<span><span class="token table-line"><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token punctuation" style="color: rgb(56, 58, 66);">------</span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token punctuation" style="color: rgb(56, 58, 66);">-------------------------------</span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span></span>
<span><span class="token table-data-rows"><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> <span class="token bold" style="font-weight: 700;"><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span><span class="token content">ML Engineer</span><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span></span> </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Full setup + training pipeline </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span></span>
<span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> <span class="token bold" style="font-weight: 700;"><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span><span class="token content">Backend Developer</span><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span></span> </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> API dependencies + model loading </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span>
<span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> <span class="token bold" style="font-weight: 700;"><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span><span class="token content">Mobile Developer</span><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span></span> </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> ONNX runtime + mobile inference </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span>
<span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> <span class="token bold" style="font-weight: 700;"><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span><span class="token content">Frontend Developer</span><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span></span> </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> None (you work separately) </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span>
<span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> <span class="token bold" style="font-weight: 700;"><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span><span class="token content">Data Analyst</span><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span></span> </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Jupyter + data access </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span>
<span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> <span class="token bold" style="font-weight: 700;"><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span><span class="token content">QA/Testing</span><span class="token punctuation" style="color: rgb(56, 58, 66);">**</span></span> </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Test environment + pytest </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span>
<span></span>
<span><span class="token hr punctuation" style="color: rgb(56, 58, 66);">---</span></span>
<span></span>
<span><span class="token title important" style="color: rgb(228, 86, 73);"><span class="token punctuation" style="color: rgb(56, 58, 66);">##</span> Prerequisites (What You Need Before Starting)</span></span>
<span></span>
<span><span class="token title important" style="color: rgb(228, 86, 73);"><span class="token punctuation" style="color: rgb(56, 58, 66);">###</span> Required Software</span></span>
<span></span>
<span><span class="token table"><span class="token table-header-row"><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-header important" style="color: rgb(228, 86, 73);"> Software </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-header important" style="color: rgb(228, 86, 73);"> Version </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-header important" style="color: rgb(228, 86, 73);"> Why You Need It </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-header important" style="color: rgb(228, 86, 73);"> Check if Installed </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span></span></span>
<span><span class="token table-line"><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token punctuation" style="color: rgb(56, 58, 66);">----------</span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token punctuation" style="color: rgb(56, 58, 66);">---------</span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token punctuation" style="color: rgb(56, 58, 66);">-----------------</span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token punctuation" style="color: rgb(56, 58, 66);">-------------------</span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span></span>
<span><span class="token table-data-rows"><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Python </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> 3.12+ </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Main programming language </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> <span class="token code-snippet code keyword" style="color: rgb(166, 38, 164);">`python --version`</span> </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span></span>
<span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> pip </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Latest </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Package installer </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> <span class="token code-snippet code keyword" style="color: rgb(166, 38, 164);">`pip --version`</span> </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span>
<span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Git </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> 2.x </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Version control </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> <span class="token code-snippet code keyword" style="color: rgb(166, 38, 164);">`git --version`</span> </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span>
<span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Virtual env </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> venv </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Isolated environment </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Built into Python </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span>
<span></span>
<span><span class="token title important" style="color: rgb(228, 86, 73);"><span class="token punctuation" style="color: rgb(56, 58, 66);">###</span> Recommended (Optional)</span></span>
<span></span>
<span><span class="token table"><span class="token table-header-row"><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-header important" style="color: rgb(228, 86, 73);"> Software </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-header important" style="color: rgb(228, 86, 73);"> Purpose </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span></span></span>
<span><span class="token table-line"><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token punctuation" style="color: rgb(56, 58, 66);">----------</span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token punctuation" style="color: rgb(56, 58, 66);">---------</span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span></span>
<span><span class="token table-data-rows"><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> VS Code </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Code editor with Python support </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span></span>
<span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Docker </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Run everything in a container </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span>
<span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> GitHub Desktop </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span><span class="token table-data"> Easier Git operations </span><span class="token punctuation" style="color: rgb(56, 58, 66);">|</span></span>
<span></span>
<span><span class="token hr punctuation" style="color: rgb(56, 58, 66);">---</span></span>
<span></span>
<span><span class="token title important" style="color: rgb(228, 86, 73);"><span class="token punctuation" style="color: rgb(56, 58, 66);">##</span> Step 1: Clone the Repository</span></span>
<span></span>
<span><span class="token title important" style="color: rgb(228, 86, 73);"><span class="token punctuation" style="color: rgb(56, 58, 66);">###</span> Option A: Using HTTPS (Easier for Beginners)</span></span>
<span></span>
<span>```bash</span>
<span><span class="token title important" style="color: rgb(228, 86, 73);"><span class="token punctuation" style="color: rgb(56, 58, 66);">#</span> Clone the main repository</span></span>
<span>git clone https://github.com/thato899/Dicovery-Grandhack.git</span>
<span></span>
<span><span class="token title important" style="color: rgb(228, 86, 73);"><span class="token punctuation" style="color: rgb(56, 58, 66);">#</span> Navigate into the ML folder</span></span>
<span>cd Dicovery-Grandhack/ml</span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong style="font-weight: 600;"><span class="">Note:</span></strong><span class=""><span> </span>If you get an authentication error, use a<span> </span></span><a href="https://github.com/settings/tokens" target="_blank" rel="noreferrer" style="color: rgb(57, 100, 254); transition: box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1); border-style: solid; border-color: rgba(255, 255, 255, 0); border-image: initial; border-width: 2px 3px; margin-left: -3px; margin-right: -3px; text-decoration: none; position: relative;"><span class="">Personal Access Token</span></a><span class=""><span> </span>instead of your password.</span></p><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Option B: Using SSH (For Advanced Users)</span></h3><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">bash</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Clone using SSH (requires SSH key setup)</span></span>
<span><span class="token function" style="color: rgb(64, 120, 242);">git</span> clone git@github.com:thato899/Dicovery-Grandhack.git</span>
<span><span class="token builtin class-name" style="color: rgb(80, 161, 79);">cd</span> Dicovery-Grandhack/ml</span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Verify You're in the Right Place</span></h3><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">bash</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># This command should show you're in the ml folder</span></span>
<span><span class="token builtin class-name" style="color: rgb(80, 161, 79);">pwd</span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Expected output: .../Dicovery-Grandhack/ml</span></span>
<span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># List files - you should see these folders:</span></span>
<span><span class="token function" style="color: rgb(64, 120, 242);">ls</span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Expected: data/  src/  tests/  notebooks/  scripts/  requirements.txt</span></span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><hr style="background: none 0% 0% / auto repeat scroll padding-box border-box rgba(0, 0, 0, 0.1); border-width: medium; border-style: none; border-color: currentcolor; border-image: initial; height: 1px; margin: 32px 0px; display: block; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><h2 style="font: 700 22px / 32px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Step 2: Create a Virtual Environment</span></h2><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Why Do We Need This?</span></h3><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">A virtual environment keeps your project's dependencies separate from other Python projects. This prevents "works on my machine" problems.</span></p><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">On Linux/Mac:</span></h3><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">bash</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Create the virtual environment</span></span>
<span>python3 <span class="token parameter variable" style="color: rgb(64, 120, 242);">-m</span> venv venv</span>
<span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Activate it</span></span>
<span><span class="token builtin class-name" style="color: rgb(80, 161, 79);">source</span> venv/bin/activate</span>
<span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Your terminal prompt should now show (venv) at the beginning</span></span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">On Windows (Command Prompt):</span></h3><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">bash</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Create the virtual environment</span></span>
<span>python <span class="token parameter variable" style="color: rgb(64, 120, 242);">-m</span> venv venv</span>
<span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Activate it</span></span>
<span>venv<span class="token punctuation" style="color: rgb(56, 58, 66);">\</span>Scripts<span class="token punctuation" style="color: rgb(56, 58, 66);">\</span>activate</span>
<span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Your terminal prompt should now show (venv) at the beginning</span></span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">On Windows (PowerShell):</span></h3><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">bash</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Create the virtual environment</span></span>
<span>python <span class="token parameter variable" style="color: rgb(64, 120, 242);">-m</span> venv venv</span>
<span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Activate it</span></span>
<span>.<span class="token punctuation" style="color: rgb(56, 58, 66);">\</span>venv<span class="token punctuation" style="color: rgb(56, 58, 66);">\</span>Scripts<span class="token punctuation" style="color: rgb(56, 58, 66);">\</span>Activate.ps1</span>
<span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># If you get an error, run this first:</span></span>
<span>Set-ExecutionPolicy <span class="token parameter variable" style="color: rgb(64, 120, 242);">-ExecutionPolicy</span> RemoteSigned <span class="token parameter variable" style="color: rgb(64, 120, 242);">-Scope</span> CurrentUser</span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Verify Virtual Environment is Active</span></h3><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">bash</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># This should show the path to your venv folder</span></span>
<span><span class="token function" style="color: rgb(64, 120, 242);">which</span> python</span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># On Windows: where python</span></span>
<span></span>
<span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Expected output includes "venv" in the path</span></span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">How to Deactivate (When You're Done)</span></h3><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">bash</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span>deactivate</span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><hr style="background: none 0% 0% / auto repeat scroll padding-box border-box rgba(0, 0, 0, 0.1); border-width: medium; border-style: none; border-color: currentcolor; border-image: initial; height: 1px; margin: 32px 0px; display: block; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><h2 style="font: 700 22px / 32px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Step 3: Install Dependencies</span></h2><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Upgrade pip first (important!)</span></h3><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">bash</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span>pip <span class="token function" style="color: rgb(64, 120, 242);">install</span> <span class="token parameter variable" style="color: rgb(64, 120, 242);">--upgrade</span> pip</span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Install Production Dependencies</span></h3><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">bash</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span>pip <span class="token function" style="color: rgb(64, 120, 242);">install</span> <span class="token parameter variable" style="color: rgb(64, 120, 242);">-r</span> requirements.txt</span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">Install Development Dependencies (Optional)</span></h3><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px 11px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"><div class="d2a24f03" style="flex-shrink: 0;"><span class="d813de27" style="color: rgb(15, 17, 21); font-family: Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin-left: 8px; font-size: 12px; line-height: 18px;">bash</span></div></div></div></div><pre style="font: 400 13px / 22px Menlo, Monaco, Consolas, &quot;Cascadia Mono&quot;, &quot;Ubuntu Mono&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;, Cousine, &quot;Roboto Mono&quot;, &quot;Courier New&quot;, Courier, sans-serif, system-ui; margin: 0px !important; overflow: auto; white-space: pre-wrap; word-break: break-all; padding: 16px;"><span><span class="token comment" style="color: rgb(160, 161, 167); font-style: italic;"># Only needed if you're writing code or running tests</span></span>
<span>pip <span class="token function" style="color: rgb(64, 120, 242);">install</span> <span class="token parameter variable" style="color: rgb(64, 120, 242);">-r</span> dev-requirements.txt</span></pre><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _33882ae"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 12 12" fill="none" class="_9bc997d _28d7e84"><path d="M-5.24537e-07 0C-2.34843e-07 6.62742 5.37258 12 12 12L0 12L-5.24537e-07 0Z" fill="currentColor"></path></svg></div><h3 style="font: 700 20px / 30px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; margin: 32px 0px 16px; color: rgb(15, 17, 21); letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><span class="">What Each Dependency Does (For Your Understanding)</span></h3><div class="ds-scroll-area ds-scroll-area--show-on-focus-within ds-scroll-area--enabled _1210dd7 c03cafe9" style="--dsl-scroll-area-gutters-disappear-delay: 1s; z-index: 0; position: relative; overflow: auto; scrollbar-width: none; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="ds-scroll-area__gutters" style="--dsl-scroll-area-scrollbar-bg: #e5e5e5; --dsl-scroll-area-scrollbar-hover: #d4d4d4; --dsl-scroll-area-horizontal-gutter-padding: 2px 0; --dsl-scroll-area-vertical-gutter-padding: 0 2px; pointer-events: none; z-index: 1000; transition: opacity 0.1s ease-out 1s; opacity: 1 !important; display: block; --container-height: 460px; position: sticky; top: 0px; left: 0px; right: 0px; width: 752px; height: 0px;"><div class="ds-scroll-area__horizontal-gutter" style="position: absolute; padding: 2px 0px; left: 0px; right: 0px; display: block; top: 446px; height: 10px;"></div><div class="ds-scroll-area__vertical-gutter" style="position: absolute; padding: 0px 2px; right: 0px; top: 8px; bottom: -452px; width: 10px;"></div></div>
Package | Purpose | Who Needs It
-- | -- | --
xgboost | Risk prediction model | ML Engineer
scikit-learn | Data preprocessing | ML Engineer, Data Analyst
pandas | Data manipulation | Everyone
numpy | Math operations | Everyone
networkx | Graph/pathfinding | ML Engineer, Backend
onnx | Model export to mobile | ML Engineer, Mobile Dev
mlflow | Track experiments | ML Engineer
optuna | Auto-tune parameters | ML Engineer
pytest | Run tests | QA, ML Engineer

</div><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong style="font-weight: 600;"><span class="">Open an issue on GitHub:</span></strong><span class=""><span> </span></span><a href="https://github.com/thato899/Dicovery-Grandhack/issues" target="_blank" rel="noreferrer" style="color: rgb(57, 100, 254); transition: box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1); border-style: solid; border-color: rgba(255, 255, 255, 0); border-image: initial; border-width: 2px 3px; margin-left: -3px; margin-right: -3px; text-decoration: none; position: relative;"><span class="">https://github.com/thato899/Dicovery-Grandhack/issues</span></a></p><hr style="background: none 0% 0% / auto repeat scroll padding-box border-box rgba(0, 0, 0, 0.1); border-width: medium; border-style: none; border-color: currentcolor; border-image: initial; height: 1px; margin: 32px 0px; display: block; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><p class="ds-markdown-paragraph" style="margin: 16px 0px; color: rgb(15, 17, 21); font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">*<span class="">Setup time: 10-15 minutes</span>*<span class=""></span><br><span class=""></span><em><span class="">Last updated: June 2026</span></em></p><div class="md-code-block md-code-block-light" style="--dsl-code-block-banner-background-color: #f9fafb; --dsl-code-block-border-radius: 12px; --dsl-code-block-banner-font: 13px/20px &quot;quote-cjk-patch&quot;, &quot;Inter&quot;, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; --dsl-code-block-content-font: 13px/22px Menlo, Monaco,  Consolas, &quot;Cascadia Mono&quot;,  &quot;Ubuntu Mono&quot;,  &quot;DejaVu Sans Mono&quot;,  &quot;Liberation Mono&quot;,  &quot;JetBrains Mono&quot;, &quot;Fira Code&quot;,  Cousine,  &quot;Roboto Mono&quot;,  &quot;Courier New&quot;, Courier,  sans-serif, system-ui; color: rgb(15, 17, 21); background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); border-radius: 12px; margin: 16px 0px; position: relative; font-family: quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><div class="md-code-block-banner-wrap" style="top: 0px; z-index: 6; background-color: rgb(255, 255, 255); border-top-left-radius: 12px; border-top-right-radius: 12px; position: sticky;"><div class="md-code-block-banner md-code-block-banner-lite" style="background: none 0% 0% / auto repeat scroll padding-box border-box rgb(249, 250, 251); font: 400 13px / 20px quote-cjk-patch, Inter, system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen, Ubuntu, Cantarell, &quot;Open Sans&quot;, &quot;Helvetica Neue&quot;, sans-serif; justify-content: space-between; padding: 0px; display: flex; border-top-left-radius: 12px; border-top-right-radius: 12px;"><div class="_121d384" style="justify-content: space-between; align-items: center; width: 740px; padding: 6px; display: flex;"></div></div></div></div><br class="Apple-interchange-newline"><!--EndFragment-->
</body>
</html>markdown
# Setup & Installation Guide

## Who Is This Guide For?

| Role | What You Need From This Guide |
|------|-------------------------------|
| **ML Engineer** | Full setup + training pipeline |
| **Backend Developer** | API dependencies + model loading |
| **Mobile Developer** | ONNX runtime + mobile inference |
| **Frontend Developer** | None (you work separately) |
| **Data Analyst** | Jupyter + data access |
| **QA/Testing** | Test environment + pytest |

---

## Prerequisites (What You Need Before Starting)

### Required Software

| Software | Version | Why You Need It | Check if Installed |
|----------|---------|-----------------|-------------------|
| Python | 3.12+ | Main programming language | `python --version` |
| pip | Latest | Package installer | `pip --version` |
| Git | 2.x | Version control | `git --version` |
| Virtual env | venv | Isolated environment | Built into Python |

### Recommended (Optional)

| Software | Purpose |
|----------|---------|
| VS Code | Code editor with Python support |
| Docker | Run everything in a container |
| GitHub Desktop | Easier Git operations |

---

## Step 1: Clone the Repository

### Option A: Using HTTPS (Easier for Beginners)

```bash
# Clone the main repository
git clone https://github.com/thato899/Dicovery-Grandhack.git

# Navigate into the ML folder
cd Dicovery-Grandhack/ml
Note: If you get an authentication error, use a [Personal Access Token](https://github.com/settings/tokens) instead of your password.

Option B: Using SSH (For Advanced Users)
bash
# Clone using SSH (requires SSH key setup)
git clone git@github.com:thato899/Dicovery-Grandhack.git
cd Dicovery-Grandhack/ml
Verify You're in the Right Place
bash
# This command should show you're in the ml folder
pwd
# Expected output: .../Dicovery-Grandhack/ml

# List files - you should see these folders:
ls
# Expected: data/  src/  tests/  notebooks/  scripts/  requirements.txt
Step 2: Create a Virtual Environment
Why Do We Need This?
A virtual environment keeps your project's dependencies separate from other Python projects. This prevents "works on my machine" problems.

On Linux/Mac:
bash
# Create the virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Your terminal prompt should now show (venv) at the beginning
On Windows (Command Prompt):
bash
# Create the virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Your terminal prompt should now show (venv) at the beginning
On Windows (PowerShell):
bash
# Create the virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1

# If you get an error, run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Verify Virtual Environment is Active
bash
# This should show the path to your venv folder
which python
# On Windows: where python

# Expected output includes "venv" in the path
How to Deactivate (When You're Done)
bash
deactivate
Step 3: Install Dependencies
Upgrade pip first (important!)
bash
pip install --upgrade pip
Install Production Dependencies
bash
pip install -r requirements.txt
Install Development Dependencies (Optional)
bash
# Only needed if you're writing code or running tests
pip install -r dev-requirements.txt
What Each Dependency Does (For Your Understanding)
Package	Purpose	Who Needs It
xgboost	Risk prediction model	ML Engineer
scikit-learn	Data preprocessing	ML Engineer, Data Analyst
pandas	Data manipulation	Everyone
numpy	Math operations	Everyone
networkx	Graph/pathfinding	ML Engineer, Backend
onnx	Model export to mobile	ML Engineer, Mobile Dev
mlflow	Track experiments	ML Engineer
optuna	Auto-tune parameters	ML Engineer
pytest	Run tests	QA, ML Engineer
Verify Installation
bash
# This command imports all packages silently
python -c "import xgboost, sklearn, pandas, numpy, networkx, onnx, onnxruntime; print('✅ All packages installed successfully!')"
Expected output:

text
✅ All packages installed successfully!
Step 4: Set Up Environment Variables
Create a .env file in the ml/ folder to store configuration:

bash
# Create the .env file
touch .env
# On Windows: type nul > .env
Add this content to .env:

bash
# Data paths
RAW_DATA_PATH=./data/raw
PROCESSED_DATA_PATH=./data/processed
FEATURES_DATA_PATH=./data/features
MODEL_PATH=./models/production

# MLflow tracking (for experiment logging)
MLFLOW_TRACKING_URI=./mlruns
MLFLOW_EXPERIMENT_NAME=saferoute_ml

# Model hyperparameters (default values)
DEFAULT_MAX_DEPTH=6
DEFAULT_LEARNING_RATE=0.1
DEFAULT_N_ESTIMATORS=100

# API settings (for backend integration)
API_PORT=8000
API_HOST=localhost

# Logging
LOG_LEVEL=INFO
LOG_FILE=./logs/training.log
Load Environment Variables (Optional)
python
# In Python code, load with:
from dotenv import load_dotenv
load_dotenv()
Step 5: Create Folder Structure
Run this script to create all necessary folders:

bash
# Create main data folders
mkdir -p data/raw
mkdir -p data/processed
mkdir -p data/features
mkdir -p data/validation
mkdir -p data/samples

# Create source code folders
mkdir -p src/data
mkdir -p src/features
mkdir -p src/models
mkdir -p src/pathfinding
mkdir -p src/api

# Create test folders (mirrors src/)
mkdir -p tests/data
mkdir -p tests/features
mkdir -p tests/models
mkdir -p tests/pathfinding

# Create other folders
mkdir -p notebooks
mkdir -p scripts
mkdir -p models/registry
mkdir -p models/staging
mkdir -p models/production
mkdir -p models/archived
mkdir -p configs
mkdir -p reports
mkdir -p logs
Verify Folder Structure
bash
# List all folders - you should see:
ls -la
# data/  src/  tests/  notebooks/  scripts/  models/  configs/  reports/  logs/
Step 6: Generate Sample Data (For Testing)
Before you can train a model, you need data. Use the sample data generator:

bash
# Run the sample data generator
python data/samples/generate_sample_data.py
Expected output:

text
Generating 1000 crime samples...
Generating 500 community report samples...
Generating 10000 environmental samples...
Sample data generated successfully!
Verify data was created:

bash
ls data/raw/
# Should see: crime_data.csv  community_reports.csv  environmental_data.csv
Step 7: Test Your Setup
Test 1: Import All Modules
bash
python -c "
from src.data.schemas import CrimeRecord, CommunityReport
from src.features.crime_features import CrimeFeatureEngineer
from src.models.risk_model import RiskModel
from src.pathfinding.a_star import RiskAwareAStar
print('✅ All modules import successfully')
"
Test 2: Run the Test Suite
bash
# Run all tests
pytest tests/ -v

# Expected: Many tests passing, some skipped (that's OK for now)
Test 3: Quick Feature Engineering Test
bash
python -c "
import pandas as pd
from src.features.pipeline import FeaturePipeline

# Load sample data
crime_df = pd.read_csv('data/raw/crime_data.csv')
locations = pd.DataFrame({
    'latitude': [-26.195],
    'longitude': [28.034],
    'timestamp': ['2026-06-01 20:00:00']
})

# Create features
pipeline = FeaturePipeline(crime_df)
features = pipeline.transform(locations)
print('Features created:', features.columns.tolist())
"
Expected output:

text
Features created: ['crime_density', 'crime_severity', 'hour_sin', ...]
Step 8: (Optional) Docker Setup
If you want to run everything in a container (guaranteed to work on any machine):

Create a Dockerfile
bash
cat > Dockerfile << 'EOF'
FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Run tests by default
CMD ["pytest", "tests/", "-v"]
EOF
Build and Run with Docker
bash
# Build the image
docker build -t saferoute-ml .

# Run the container
docker run -it saferoute-ml

# Run with data mounted
docker run -it -v $(pwd)/data:/app/data saferoute-ml python scripts/run_training.py
Troubleshooting Common Setup Issues
Issue 1: "pip: command not found"
Solution:

bash
# On Linux/Mac
python3 -m ensurepip

# On Windows
python -m ensurepip
Issue 2: "Permission denied" when creating venv
Solution:

bash
# On Linux/Mac
sudo chown -R $USER:$USER ~/Dicovery-Grandhack

# Or use a different location
cd ~
python3 -m venv saferoute_venv
Issue 3: "No module named _ctypes" when creating venv
Solution:

bash
# On Linux (Ubuntu/Debian)
sudo apt-get install libffi-dev

# On Mac
brew install libffi

# Then recreate venv
rm -rf venv
python3 -m venv venv
Issue 4: "Command not found: pytest" after installing
Solution:

bash
# Ensure virtual environment is activated
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Reinstall pytest
pip install --upgrade pytest
Issue 5: Git asks for password every time
Solution:

bash
# Cache credentials for 1 hour
git config --global credential.helper 'cache --timeout=3600'

# Or store permanently
git config --global credential.helper store
# Next push will ask for credentials and save them
Issue 6: "ERROR: Could not find a version that satisfies the requirement"
Solution:

bash
# Upgrade pip and try again
pip install --upgrade pip
pip install --upgrade setuptools wheel

# Then retry
pip install -r requirements.txt
Quick Start Commands (Cheat Sheet)
bash
# === ONE-TIME SETUP ===
git clone https://github.com/thato899/Dicovery-Grandhack.git
cd Dicovery-Grandhack/ml
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python data/samples/generate_sample_data.py

# === EVERY TIME YOU WORK ===
cd ~/Dicovery-Grandhack/ml
source venv/bin/activate  # On Windows: venv\Scripts\activate

# === TRAIN A MODEL ===
python scripts/run_training.py

# === RUN TESTS ===
pytest tests/ -v

# === START JUPYTER ===
jupyter notebook notebooks/

# === EXPORT TO ONNX ===
python scripts/export_model.py

# === WHEN YOU'RE DONE ===
deactivate
For Different Roles: What to Install
Minimal Setup (For Non-Coders / Reviewers)
If you just want to review documentation and not run code:

bash
# No installation needed! Just read the wiki pages.
# Start here: https://github.com/thato899/Dicovery-Grandhack/wiki
Data Analyst Setup
bash
pip install pandas numpy jupyter matplotlib seaborn
# Then run: jupyter notebook
Mobile Developer Setup (Only ONNX)
bash
# You don't need the full Python environment
# Just download the exported .onnx file from:
# https://github.com/thato899/Dicovery-Grandhack/blob/main/ml/models/production/risk_model.onnx
Backend Developer Setup
bash
pip install fastapi uvicorn pydantic
# You'll call the model via API, not directly
Full ML Engineer Setup (All of the above)
bash
# Follow all steps in this guide
Next Steps After Setup
Read the documentation:

[Data Models & Schemas](https://data-models-schemas/)

[Feature Engineering](https://feature-engineering/)

[Model Training](https://model-training/)

Run your first training:

bash
python scripts/run_training.py
Explore with Jupyter:

bash
jupyter notebook notebooks/01_exploratory_analysis.ipynb
Check the model evaluation:

bash
python scripts/run_evaluation.py
Export for mobile:

bash
python scripts/export_model.py
Still Stuck?
Problem	Who to Ask
Git/Clone issues	Team Lead
Python/venv issues	ML Engineer
Package installation	Any developer
Permission errors	System Admin
Docker issues	DevOps
Open an issue on GitHub: https://github.com/thato899/Dicovery-Grandhack/issues

*Setup time: 10-15 minutes*
Last updated: June 2026