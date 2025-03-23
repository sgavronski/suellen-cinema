from view.html import style, menu


script_salvar_filme = '''
    var form = document.getElementById('myForm');

    function salvarFilme() {
        var xhr = new XMLHttpRequest();
        var formData = new FormData(form);

        // Open the request.
        xhr.open('POST',' http://127.0.0.1:8000/filme')
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

cadastro_filme = f'''
    <!DOCTYPE html> 
    <html>
        <head>
            {style}
        </head>
        <body> 
            <form id="myForm" action="javascript:salvarFilme()">
                <label for="fname">Título:</label>
                <input type="text" id="titulo" name="titulo"><br><br>

                <label for="lname">Ano:</label>
                <input type="text" id="ano" name="ano"><br><br>

                <label for="lname">Valor:</label>
                <input type="text" id="valor" name="valor"><br><br>

                <label for="lname">Genero:</label>
                <input type="text" id="genero" name="genero"><br><br>

                <input type="submit" value="Submit">
            </form>

             <footer>
                {menu}
             </footer>

            <script type="text/javascript">
                {script_salvar_filme}
            </script>
        </body> 
    </html>
'''

script_listar_filmes = '''
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:8000/filmes');
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

lista_filmes = f'''
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
                {script_listar_filmes}
            </script>
        </body> 
    </html>
'''