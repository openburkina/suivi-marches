export function pieStatAdapter(input_data) {
    let labels = ["Planification", "Lancement", "Attribution", "Contractualisation", "Implémentation", "Terminé"]
    let data = [
        input_data['planning'],
        input_data['tender'],
        input_data['award'],
        input_data['contract'],
        input_data['implementation'],
        input_data['done'],
    ]
    return {labels: labels, data: data} 
}

export function lineStatAdapter(input_data, start_year, end_year) {
    let labels = []
    let data = []
    for (let i = 0; i <= parseInt(end_year) - parseInt(start_year); i++) {
        labels.push(i + parseInt(start_year))
    }
    let a = input_data.reduce(function (r, a) {
        r[a.sector] = r[a.sector] || {};
        r[a.sector][a.year] = a.value;
        return r;
    }, Object.create(null));
    for (let [k, v] of Object.entries(a)) {
        let new_data = labels.map((year_value, i) => v[start_year+i] || 0 )
        data.push({name: k, data: new_data})
    }
    return {labels, data} 
}

export function barStatAdapter(input_data) {
    let labels = []
    let data = []
    for (let o of input_data) {
        labels.push(o.name)
        data.push(o.value)
    }
    return {labels, data} 
}