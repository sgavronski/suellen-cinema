
style = '''
    <style>
        table {
          font-family: arial, sans-serif;
          border-collapse: collapse;
          width: 100%;
        }

        td, th {
          border: 1px solid #dddddd;
          text-align: left;
          padding: 8px;
        }

        tr:nth-child(even) {
          background-color: #dddddd;
        }

        footer {
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
'''


menu = '''
    <table>
        <tr>
            <th>Entidades</th>
            <th>Listagens</th>
            <th>Cadastros</th>
        </tr>
        <tr>
            <td>Pessoas</td>
            <td>
                <a href="http://127.0.0.1:8000/html/pessoas/lista">
                    <button>Listar</button>
                </a>
            </td>
            <td>
                <a href="http://127.0.0.1:8000/html/pessoas/cadastro">
                    <button>Cadastrar</button>
                </a>
            </td>
        </tr>
        <tr>
           <td>Filmes</td>
            <td>
                <a href="http://127.0.0.1:8000/html/filmes/lista">
                    <button>Listar</button>
                </a>
            </td>
            <td>
                <a href="http://127.0.0.1:8000/html/filmes/cadastro_filme">
                    <button>Cadastrar</button>
                </a>
            </td>
        </tr>
        <tr>
            <td colspan="3">
                <a href="http://127.0.0.1:8000/html">
                    <button>Voltar ao Inicio</button>
                </a>
            </td>
        </tr>
    </table>
'''
