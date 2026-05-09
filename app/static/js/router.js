const pages = {
        "/home": `
                <div class="container">
                    <h1>Painel Principal</h1>
                    <p>Selecione uma categoria acima para gerenciar os cadastros do Pet Vida.</p>
                </div>`,

        "/clientes": `
                <div class="container">
                    <h1>Cadastro de Clientes</h1>
                    <form method="POST">
                        <input type="text" name="nome" placeholder="Nome" required>
                        <input type="text" name="telefone" placeholder="Telefone" required>
                        <input type="email" name="email" placeholder="E-mail" required>
                        <button type="submit">Cadastrar</button>
                    </form>
                    <div class="box">
                        <h2>Clientes cadastrados</h2>
                        <table>
                            <thead><tr><th>ID</th><th>Nome</th><th>Telefone</th><th>E-mail</th></tr></thead>
                            <tbody>{% for cliente in clientes %}<tr><td>{{ cliente[0] }}</td><td>{{ cliente[1] }}</td><td>{{ cliente[2] }}</td><td>{{ cliente[3] }}</td></tr>{% endfor %}</tbody>
                        </table>
                    </div>
                </div>`,

        "/pets": `
                <div class="container">
                    <h1>Cadastro de Pets</h1>
                    <form method="POST">
                        <input type="text" name="nome" placeholder="Nome do pet" required>
                        <input type="text" name="tipo" placeholder="Tipo do pet" required>
                        <input type="text" name="raça" placeholder="Raça" required>
                        <button type="submit">Cadastrar</button>
                    </form>
                    <div class="box">
                        <h2>Pets cadastrados</h2>
                        <table>
                            <thead><tr><th>ID</th><th>Nome</th><th>Tipo</th><th>Raça</th></tr></thead>
                            <tbody>{% for pet in pets %}<tr><td>{{ pet[0] }}</td><td>{{ pet[1] }}</td><td>{{ pet[2] }}</td><td>{{ pet[3] }}</td></tr>{% endfor %}</tbody>
                        </table>
                    </div>
                </div>`,

        "/servicos": `
                <div class="container">
                    <h1>Serviços (Banho e Tosa)</h1>
                    <form method="POST">
                        <input type="text" name="pet_atendido" placeholder="Nome do Pet" required>
                        <input type="text" name="tipo" placeholder="Tipo do serviço" required>
                        <input type="date" name="data" required>
                        <input type="text" name="valor" placeholder="Valor" required>
                        <button type="submit">Cadastrar</button>
                    </form>
                    <div class="box">
                        <h2>Serviços cadastrados</h2>
                        <table>
                            <thead><tr><th>ID</th><th>Tipo</th><th>Valor</th><th>Data</th></tr></thead>
                            <tbody>{% for serviço in serviços %}<tr><td>{{ serviço[0] }}</td><td>{{ serviço[1] }}</td><td>{{ serviço[2] }}</td><td>{{ serviço[3] }}</td></tr>{% endfor %}</tbody>
                        </table>
                    </div>
                </div>`,

        "/fornecedores": `
                <div class="container">
                    <h1>Fornecedores</h1>
                    <form method="POST">
                        <input type="text" name="nome" placeholder="Nome" required>
                        <input type="text" name="telefone" placeholder="Telefone" required>
                        <input type="text" name="produto" placeholder="Produto fornecido" required>
                        <button type="submit">Cadastrar</button>
                    </form>
                    <div class="box">
                        <h2>Fornecedores cadastrados</h2>
                        <table>
                            <thead><tr><th>ID</th><th>Nome</th><th>Telefone</th><th>Produto</th></tr></thead>
                            <tbody>{% for fornecedor in fornecedores %}<tr><td>{{ fornecedor[0] }}</td><td>{{ fornecedor[1] }}</td><td>{{ fornecedor[4] }}</td></tr>{% endfor %}</tbody>
                        </table>
                    </div>
                </div>`,

        "/vendas": `
                <div class="container">
                    <h1>Vendas</h1>
                    <form method="POST">
                        <input type="text" name="cliente" placeholder="Nome do cliente" required>
                        <input type="text" name="produto" placeholder="Produto vendido" required>
                        <input type="text" name="valor" placeholder="Valor total" required>
                        <button type="submit">Cadastrar</button>
                    </form>
                    <div class="box">
                        <h2>Vendas cadastradas</h2>
                        <table>
                            <thead><tr><th>ID</th><th>Cliente</th><th>Data</th><th>Valor</th></tr></thead>
                            <tbody>{% for venda in vendas %}<tr><td>{{ venda[0] }}</td><td>{{ venda[1] }}</td><td>{{ venda[3] }}</td><td>{{ venda[4] }}</td></tr>{% endfor %}</tbody>
                        </table>
                    </div>

                </div>`,

        "/sobre": `<div class="container"><h1>Sobre</h1><p>Sistema Pet Vida v1.0</p></div>`,
        "/contato": `<div class="container"><h1>Contato</h1><p>Email: suporte@petvida.com</p></div>`,
      };

      function navigate(path) {
        window.location.hash = path;
      }

      window.addEventListener("hashchange", () => {
        const path = location.hash.replace("#", "") || "/home";
        document.getElementById("app").innerHTML =
          pages[path] || "<h1>404</h1>";
      });

      // Inicialização
      if (!window.location.hash) {
        navigate("/home");
      } else {
        window.dispatchEvent(new HashChangeEvent("hashchange"));
      }