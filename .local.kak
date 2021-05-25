hook -group latex global WinSetOption filetype=latex %{
  set window autoreload true
  lsp-auto-signature-help-disable
  addhl -override window/wrap wrap -word -marker ">" 
  set window autowrap_column 120
  autowrap-enable 
}
hook -group latex global BufWritePost .*\.(tex) %{
  nop %sh{ 
    latexindent -w -m -l=.latexindent.yaml $kak_reg_percent
    rm "${kak_reg_percent/.tex/.bak}"
  }
}
