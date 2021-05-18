set global autoreload true
addhl -override global/wrap wrap -word -marker ">" 
hook -group latex global BufWritePost .*\.(tex) %{
  nop %sh{ 
    latexindent -w -m -l=.latexindent.yaml $kak_reg_percent
    rm "${kak_reg_percent/.tex/.bak}"
  }
}
