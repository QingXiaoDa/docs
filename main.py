def define_env(env):
    @env.macro
    def paper(tag, date, title, desc, url=None):
        return f""" 
<div class="paper-row">
  <div class="paper-meta">
    <div class="paper-tag">{tag}</div>
    <div class="paper-date">{date}</div>
  </div>
  <div class="paper-content">
    <h3 class="paper-title"><a href="{url}" target="_blank">{title}</a></h3>
    <p class="paper-desc">{desc}</p>
  </div>
</div>
"""
