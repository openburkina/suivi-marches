// We put there all our actions, ie all our async functions(to request our api)
import axios from 'axios'
export const myActions=({commit})=>{
    axios.get("http://0.0.0.0:8000/hello").then((res)=>{
        console.log(res.data)
        commit('getAllData',res.data)
    })
}