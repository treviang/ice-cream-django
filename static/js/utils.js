document.addEventListener('DOMContentLoaded', function () {
    let miscelaForm = document.querySelectorAll(".miscela-form")
    let addIngrediente = document.querySelector("#add-ingrediente")
    let totalForms = document.querySelector("#id_form-TOTAL_FORMS")
    let tabella = document.getElementById('ingredienti-table');


    let formNum = miscelaForm.length - 1
    addIngrediente.addEventListener('click', addForm)

    function addForm(e) {
        e.preventDefault()

        let newForm = miscelaForm[0].cloneNode(true)
        let formRegex = RegExp(`form-(\\d){1}-`, 'g')

        formNum++
        newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
        tabella.appendChild(newForm)

        totalForms.setAttribute('value', `${formNum + 1}`)
    }

    let selectIngrediente = document.querySelector('.sel-ingrediente');
    selectIngrediente.addEventListener('change', showOnChange);

    function showOnChange(e) {
        var selectedOption = e.target.value;

        let options = {
            method: 'GET',
            headers: {}
        };

        fetch('/get_ingrediente/' + selectedOption, options)
            .then(response => response.json())
            .then(body => {
                document.getElementById('costo').innerHTML = body[0].costo;
            });

    }
})