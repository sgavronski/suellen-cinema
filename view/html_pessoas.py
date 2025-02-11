from view.html import style, menu


script_salvar_pessoa = '''
    var form = document.getElementById('myForm');
    
    function salvarPessoa() {
        var xhr = new XMLHttpRequest();
        var formData = new FormData(form);
    
        // Open the request.
        xhr.open('POST',' http://127.0.0.1:8000/pessoa')
        xhr.setRequestHeader("Content-Type", "application/json");
    
        // Send the form data.
        var json = JSON.stringify(Object.fromEntries(formData));
        xhr.send(json);
    
        xhr.onreadystatechange = function() {
            if (xhr.readyState == XMLHttpRequest.DONE) {
                alert("Salvo com Sucesso!");
                form.reset(); //reset form after AJAX success or do something else
            }
        }
        //Fail the onsubmit to avoid page refresh.
        return false; 
    }
'''


script_listar_pessoas = '''
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:8000/pessoas');
    xhr.responseType = 'json';
    xhr.onload = function(e) {
        if (this.status == 200) {
            var data = this.response;
            var table = document.createElement('table');

            /* 
             * Create table columns. 
             */
            var tr = document.createElement('tr');
            var firstObject  = data[0];
            for (const [key, value] of Object.entries(firstObject)) {
                var th = document.createElement('th');
                th.appendChild(document.createTextNode(key));
                tr.appendChild(th);
            }

            // Add columns in the table.
            table.appendChild(tr);


            /* 
             * Create table values. 
             */
            data.forEach(function(object) {
                tr = document.createElement('tr');
                for (const [key, value] of Object.entries(object)) {
                    var td = document.createElement('td');
                    td.appendChild(document.createTextNode(value));
                    tr.appendChild(td);
                }

                // Add values in the table.
                table.appendChild(tr);
            });

            document.body.appendChild(table);
        }
    };
    xhr.send();
'''


cadastro = f'''
    <!DOCTYPE html> 
    <html>
        <head>
            {style}
        </head>
        <body> 
            <form id="myForm" action="javascript:salvarPessoa()">
                <label for="fname">Nome:</label>
                <input type="text" id="nome" name="nome"><br><br>

                <label for="lname">Sobrenome:</label>
                <input type="text" id="sobrenome" name="sobrenome"><br><br>

                <label for="lname">Idade:</label>
                <input type="text" id="idade" name="idade"><br><br>

                <label for="lname">Genero:</label>
                <input type="text" id="genero" name="genero"><br><br>

                <label for="lname">Endereco:</label>
                <input type="text" id="endereco" name="endereco"><br><br>

                <label for="lname">Telefone:</label>
                <input type="text" id="telefone" name="telefone"><br><br>

                <input type="submit" value="Submit">
            </form>
            
             <footer>
                {menu}
             </footer>

            <script type="text/javascript">
                {script_salvar_pessoa}
            </script>
        </body> 
    </html>
'''


lista = f'''
    <!DOCTYPE html> 
    <html>
        <head>
            {style}
        </head>
        <body>
            <footer>
                {menu}
            </footer>
            <script type="text/javascript">
                {script_listar_pessoas}
            </script>
        </body> 
    </html>
'''
