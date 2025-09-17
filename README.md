# 🧮 Calculadora de Salário Líquido - Flask

Este projeto é uma aplicação web desenvolvida em **Python** utilizando o framework **Flask**.  
Ela permite calcular o **salário líquido** a partir do salário bruto e do número de dependentes, considerando regras simplificadas da CLT.

---

## 🚀 Funcionalidades
- Entrada de **salário bruto** e **número de dependentes** via formulário web.
- Cálculo automático dos descontos:
  - **INSS:** 8% sobre o salário bruto.
  - **IR:** 15% caso o salário bruto seja maior que **R$ 2.500,00**.
  - **Benefício por dependente:** +R$ 200,00 por dependente.
- Validação de dados:
  - Não permite valores negativos.
  - Exibe mensagens de erro diretamente na tela.
- Interface moderna e responsiva com HTML + CSS.

---


📝 Fórmula de cálculo

Salário Líquido = Salário Bruto - INSS - IR + (Dependentes * 200)

