const units = {
    ft : 0.3048,
    mi : 1609.34,
    m : 1,
    km : 1000,
    yd : 0.9144,
    in : 0.0254,
}




const userUnit = prompt('What unit are we converting from? ft / mi / m / km / yd / in')
const howMany = prompt(`How many ${userUnit}?`)
const done = howMany * units[userUnit]

alert(`${howMany} ${userUnit} is ${done} meters.`)

// I dont even know 
