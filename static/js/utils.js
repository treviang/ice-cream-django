document.addEventListener('DOMContentLoaded', function () {
    let miscelaBody = document.getElementById('miscela-body');
    let miscelaRow = document.querySelectorAll(".miscela-row")
    let addIngrediente = document.querySelector("#add-ingrediente")
    let totalForms = document.querySelector("#id_form-TOTAL_FORMS")
    let tabella = document.getElementById('ingredienti-table');


    let formNum = miscelaRow.length - 1
    addIngrediente.addEventListener('click', addForm)

    function addForm(e) {
        e.preventDefault()

        let newForm = miscelaRow[0].cloneNode(true)
        let formRegex = RegExp(`form-(\\d){1}-`, 'g')

        formNum++
        newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
        console.log(tabella.tbody)
        miscelaBody.appendChild(newForm)

        totalForms.setAttribute('value', `${formNum + 1}`)
        aggiungiListenerSelectIngredienti();
    }

    aggiungiListenerSelectIngredienti();
})

function aggiungiListenerSelectIngredienti() {
    document.querySelectorAll('.sel-ingrediente').forEach(function (element) {
        element.addEventListener('change', showOnChange);
    })
}

function showOnChange(e) {
    var selectedOption = e.target.value;

    let options = {
        method: 'GET',
        headers: {}
    };

    fetch('/get_ingrediente/' + selectedOption, options)
        .then(response => response.json())
        .then(body => {
            const lastIndex = e.target.id.lastIndexOf('-');
            let prefix = e.target.id.slice(0, lastIndex + 1);

            aggiornaCampi(body[0], prefix);
        });

}

function aggiornaCampi(ingrediente, prefix) {

    let dosaggio = Number(document.getElementById(prefix + 'dosaggio').value);

    document.getElementById(prefix + 'zuccheri').innerHTML = dosaggio * ingrediente.zuccheri;
    document.getElementById(prefix + 'grassi').innerHTML = dosaggio * ingrediente.grassi;
    document.getElementById(prefix + 'acqua').innerHTML = dosaggio * ingrediente.acqua;
    document.getElementById(prefix + 'costo').innerHTML = dosaggio * ingrediente.costo;
}