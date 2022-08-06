const toMeters = {
    ft : 0.3048,
    mi : 1609.34,
    m : 1,
    km : 1000,
    yd : 0.9144,
    in : 0.0254,
}



const distance = prompt('What is the distance?')
const from = prompt('What unit are we converting from? ft / mi / m / km / yd / in')
const to = prompt('What unit are we converting to? ft / mi / m / km / yd / in')


const result = (distance * toMeters[from]) / toMeters[to]

console.log(alert(`${distance} ${from} is equal to ${result} ${to}.`))

// ...bruh