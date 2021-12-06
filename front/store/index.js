import axios from 'axios'

export const state = () => ({
    list: null
  })

export const mutations = {
    listOfBuyers(state,paylaod){
        state.list = paylaod
    },

    setToken({state,paylaod}){
        state.token = paylaod
    }
    
}
export const actions = {
    async getToken({commit}){
        await axios.post("http://0.0.0.0:8000/auth-token/",
        {username:"AdamMusa","password":"Adaforlan"}
        ).then((res)=>commit('setToken',res.data))
    },
    async fetchBuyers({ commit }){
        await axios.get(
            "http://0.0.0.0:8080/hello",
             // "https://jsonplaceholder.typicode.com/users", 
           
          ).then(res=>{
              commit("listOfBuyers",res.data)}
            );
       
    }
}
export const getters = {}