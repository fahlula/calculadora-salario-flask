from flask import Flask, render_template, request, redirect, url_for, flash

# Criação do app Flask
app = Flask(__name__)
app.secret_key = "chave-secreta"  # Necessário para usar flash

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    try:
        # Captura os valores do formulário
        salario = float(request.form['salario'])
        dependentes = int(request.form['dependentes'])
    except ValueError:
        flash("Erro: Insira valores numéricos válidos!", "erro")
        return redirect(url_for('index'))

    # Validações básicas
    if salario < 0:
        flash("Erro: O salário não pode ser negativo.", "erro")
        return redirect(url_for('index'))

    if dependentes < 0:
        flash("Erro: O número de dependentes não pode ser negativo.", "erro")
        return redirect(url_for('index'))

    # Cálculos
    inss = salario * 0.08
    ir = salario * 0.15 if salario > 2500 else 0
    bonus_dependentes = dependentes * 200
    resultado_final = salario - inss - ir + bonus_dependentes

    # Envia os dados para o resultado.html
    return render_template(
        "resultado.html",
        salario=f"{salario:.2f}",
        inss=f"{inss:.2f}",
        ir=f"{ir:.2f}",
        dependentes=dependentes,
        dependentes_total=f"{bonus_dependentes:.2f}",
        liquido=f"{resultado_final:.2f}"
    )

if __name__ == '__main__':
    app.run(debug=True)
