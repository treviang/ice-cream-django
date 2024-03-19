document.addEventListener('DOMContentLoaded', function () {
    let miscelaBody = document.getElementById('miscela-body');
    let miscelaRow = document.querySelectorAll(".miscela-row")
    let addIngrediente = document.querySelector("#add-ingrediente")
    let totalForms = document.querySelector("#id_form-TOTAL_FORMS")

    let formNum = miscelaRow.length - 1
    addIngrediente.addEventListener('click', addForm)
    totalForms.setAttribute('value', `${formNum + 1}`)

    function addForm(e) {
        e.preventDefault()

        let newForm = miscelaRow[0].cloneNode(true)
        let formRegex = RegExp(`form-(\\d){1}-`, 'g')

        formNum++
        newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`)
        miscelaBody.appendChild(newForm)

        totalForms.setAttribute('value', `${formNum + 1}`)
        aggiungiListenerSelectIngredienti();
        aggiungiListenerInputDosaggio();
    }

    aggiungiListenerSelectIngredienti();
    aggiungiListenerInputDosaggio();
})

function aggiungiListenerSelectIngredienti() {
    document.querySelectorAll('.sel-ingrediente').forEach(function (element) {
        element.addEventListener('change', onChangeIngrediente);
        aggiornaIngredienti(element.lastElementChild);
    })
}

function aggiungiListenerInputDosaggio() {
    document.querySelectorAll('.inp-dosaggio').forEach(function (element) {
        element.addEventListener('change', onChangeDosaggio);
    })
}

function onChangeIngrediente(e) {
    aggiornaIngredienti(e.target);
}

function aggiornaIngredienti(element) {
    var selectedOption = element.value;

    if(selectedOption) {
        fetch('/get_ingrediente/' + selectedOption, {method: 'GET'})
            .then(response => response.json())
            .then(body => {
                const lastIndex = element.id.lastIndexOf('-');
                let prefix = element.id.slice(0, lastIndex + 1);
    
                aggiornaCampi(body[0], prefix);
            });
    }
}

function onChangeDosaggio(e) {
    const lastIndex = e.target.id.lastIndexOf('-');
    let prefix = e.target.id.slice(0, lastIndex + 1);

    var selectedValue = document.getElementById(prefix+'ingrediente').value;

    fetch('/get_ingrediente/' + selectedValue, {method: 'GET'})
        .then(response => response.json())
        .then(body => {
            aggiornaCampi(body[0], prefix);
        });
}

function aggiornaCampi(ingrediente, prefix) {

    let dosaggio = Number(document.getElementById(prefix + 'dosaggio').value);
    
    document.getElementById(prefix + 'zuccheri').innerHTML = calcolaPercentuale(dosaggio, ingrediente.zuccheri);
    document.getElementById(prefix + 'grassi').innerHTML = calcolaPercentuale(dosaggio, ingrediente.grassi);
    document.getElementById(prefix + 'SIng').innerHTML = calcolaPercentuale(dosaggio, ingrediente.SIng);
    document.getElementById(prefix + 'altri-solidi').innerHTML = calcolaPercentuale(dosaggio, ingrediente.altri_solidi);
    document.getElementById(prefix + 'acqua').innerHTML = calcolaPercentuale(dosaggio, ingrediente.acqua);
    document.getElementById(prefix + 'costo').innerHTML = calcolaValuta(dosaggio, ingrediente.costo);
    
    calcolaTotali()
}

function calcolaPercentuale(dosaggio, valore) {
    const percentuale = ' <span>%</span>'
    return (dosaggio * valore).toFixed(2) + percentuale;
}

function formattaTotalePercentuale(valore) {
    const percentuale = ' %'
    return valore.toFixed(2) + percentuale;
}

function calcolaValuta(dosaggio, valore) {
    const euro = ' <span>\u20AC</span>'
    return (dosaggio * valore).toFixed(4) + euro;
}

function formattaTotaleValuta(valore) {
    const euro = ' \u20AC'
    return valore.toFixed(4) + euro;
}

function calcolaTotali() {
    var final = 0
    var tfoot = document.querySelector("tfoot");
    var howManyCols = tfoot.rows[0].cells.length;
    var totalRow = tfoot.rows[tfoot.rows.length - 1];
    for (var j = 1; j < howManyCols; j++) {
        final = calcolaTotaliColonne(j);
        if (totalRow.cells[j].className === 'percentuale') {
            totalRow.cells[j].innerText = formattaTotalePercentuale(final);
        } else if (totalRow.cells[j].className === 'valuta') {
            totalRow.cells[j].innerText = formattaTotaleValuta(final);
        } else {
            totalRow.cells[j].innerText = final;
        }
    }
}

function calcolaTotaliColonne(numeroColonna) {

    var totale = 0;
    try {
        var tableBody = document.querySelector("tbody");
        var howManyRows = tableBody.rows.length;

        for (var i = 0; i < howManyRows; i++) {

            let valoreCella = 0;
            const elementoCella = tableBody.rows[i].cells[numeroColonna].childNodes.item(0)

            if (elementoCella.tagName == 'INPUT' && elementoCella.getAttribute("type") == 'number') {
                valoreCella = Number(elementoCella.value);
            } else {
                valoreCella = Number(elementoCella.data);
            }

            if (!isNaN(valoreCella))
                totale += valoreCella;
        }
    } finally {
        return totale;
    }
}