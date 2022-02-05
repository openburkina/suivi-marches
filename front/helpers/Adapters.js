export function pieStatAdapter(input_data) {
    let labels = []
    let data = []

    for (let [k, v] of Object.entries(input_data)) {
        labels.push(k)
        data.push(v)
    }
    return {labels: labels, data: data} 
}

export function lineStatAdapter(input_data, start_year, end_year) {
    let labels = []
    let data = []
//     for (let i = 0; i <= end_year - start_year; i++) {
//         labels.push(toString(i + start_year))
//     }
//     let a = input_data.reduce(function (r, a) {
//         r[a.sector] = r[a.sector] || [];
//         r[a.sector].push({'name': a.sector});
//         return r;
//     }, Object.create(null));
    // for ({ year, values } in Object.entries(input_data)) {
    //     labels.push(year)

    // }
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