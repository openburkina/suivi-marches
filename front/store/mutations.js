// We put there all our mutations, ie all our sync functions(to change value directly)

export const getAllData =(state,payload)=>{
    state.data = payload
}