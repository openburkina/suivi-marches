import axios from 'axios'

export const state = ()=>{
    buyers: []
}

export const mutations = {
    listOfBuyers({state,paylaod}){
        state.buyers = paylaod
    }
}
export const actions = {
    async fetchBuyers({commit}){
       await axios.get("http://0.0.0.0:8000/api/buyers/",
       {
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': "http://0.0.0.0:8000/api/buyers/"
            }
          }
       ).then((res)=>{commit('listOfBuyers',res)}).catch((err)=>console.log(err))
        
       
    }
}
export const getters = {}