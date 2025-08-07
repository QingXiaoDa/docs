def define_env(env):
    @env.macro
    def paper(tag, date, title, desc, url=None):
        link_html = f'<p><a href="{url}" target="_blank">阅读原文</a></p>' if url else ""
        return f""" 
<div class="paper-row">
  <div class="paper-meta">
    <div class="paper-tag">{tag}</div>
    <div class="paper-date">{date}</div>
  </div>
  <div class="paper-content">
    <h3 class="paper-title">{title}</h3>
    <p class="paper-desc">{desc}</p>
    {link_html}
  </div>
</div>
"""
