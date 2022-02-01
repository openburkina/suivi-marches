import axios from 'axios'

export const state = () => ({
    list: [],
    recordsDone: [],
    recordsInprogress:[],
    totauxByBuyer:[],
    records:[],
    tendersYear:[],
    bByRegion:[],
    listOfCleanData:[],
    stats:[],
    tmpStat:[],
    tmpList:[],
    listOfRecords:[],
    particularName:'',
    listOfRegion: [],
    listRegions:[],
    regionName:'',
    stataSerie:[],
    
  })

export const mutations = {

    // setter de Liste de tous les buyers
    listOfBuyers(state,paylaod){
        state.list = paylaod
        state.list.forEach(el => {
            console.log(el)
            state.listOfCleanData.push({
                id:el.id,
                name:el.name,
                country_name:el.address.country_name,
                locality:el.address.locality,
                latitude:el.address.locality_latitude,
                longitude:el.address.locality_longitude,
                postal:el.address.postal_code,
                region:el.address.region,
                email:el.contact_point.email,
                fax_number:el.contact_point.fax_number,
                contact_name:el.contact_point.name,
                telephone:el.contact_point.telephone,
                url:el.contact_point.url,
                uri:el.identifier.uri,
                scheme:el.identifier.scheme,
                legal_name:el.identifier.legal_name,
            })
            
        })
        state.list = state.listOfCleanData
        state.listOfCleanData = []
    },
    
    // setter de Liste de tous les travaux fait par un buyers
    listRecordsDone(state,paylaod){
        state.recordsDone = paylaod

        state.tmpList = []
        state.recordsDone.forEach((el)=>{
            state.tmpList.push({
                url:el.url,
                compiled_release:el.compiled_release,
                target_name:el.target.name,
                country:el.implementation_address.country_name,
                region:el.implementation_address.region,
                locality:el.implementation_address.locality,
                postal_code:el.implementation_address.postal_code,
                longitude:el.implementation_address.locality_longitude,
                latitude:el.implementation_address.locality_latitude,
                ocid:el.ocid,
                implementation_value:el.implementation_value
            })
           
        })
        state.recordsDone = state.tmpList
        state.tmpList = []
        state.tmpList.push(state.recordsDone.length)
        state.tmpList.push(state.recordsInprogress.length)
        state.stataSerie = state.tmpList
        state.tmpList = []
       
    },

    // setter de Liste de tous les travaux en cours par buyers
    listRecordsInprogress(state,paylaod){
        state.recordsInprogress = paylaod
        state.recordsInprogress.forEach((el)=>{
            state.tmpList.push({
                url:el.url,
                compiled_release:el.compiled_release,
                target_name:el.target.name,
                country:el.implementation_address.country_name,
                region:el.implementation_address.region,
                locality:el.implementation_address.locality,
                postal_code:el.implementation_address.postal_code,
                longitude:el.implementation_address.locality_longitude,
                latitude:el.implementation_address.locality_latitude,
                ocid:el.ocid,
                implementation_value:el.implementation_value
            })
           
        })
        state.recordsInprogress = state.tmpList
        state.tmpList = []
       
    },
    
    // setter de Liste de tous les travauxd'un buyers par region
    listTotauxBuyer(state,paylaod){
        state.totauxByBuyer = paylaod
        console.log(state.totauxByBuyer)

    },
    listOfRecords(state,paylaod){
        state.listOfRecords = paylaod
        state.listOfRecords.forEach((el)=>{
            state.tmpList.push({
                title: el.title,
                record_ocid:el.record_ocid,
                sector: el.sector,
                country: el.country,
                region: el.region,
                value: el.value,
                currency: el.currency,
                step: el.step,
                last_update: el.last_update
            })
        })
        state.listOfRecords = state.tmpList
        state.tmpList = []

    },

    // setter de Liste de tous les tenders
    listSpecification(state,paylaod){
        state.records = paylaod
        console.log(state.records)

    },
     // setter de Liste de tous les tenders
    particularRegion(state,paylaod){
        state.listRegions = paylaod
        console.log(state.listRegions)

    },
    
     // setter de Liste de tous les tenders
    getRegion(state,paylaod){
        state.listOfRegion = paylaod
        console.log(state.records)

    },
    // setter de Liste de tous les marché par année
    listTendersByYear(state,paylaod){
        state.tendersYear = paylaod
        console.log(state.tendersYear)

    },


    // { params: {
//   mail,
//   firstname
// }}
     // setter de Liste de tous les marché par année
    listBuyerByRegion(state,paylaod){
        state.bByRegion = paylaod
        console.log(state.bByRegion)

    }

}
export const actions = {
    /*
        ###################################################################
    */
    // Liste de tous les buyers
    async fetchBuyers({ commit }){
        await axios.get(
            "http://localhost:8000/api/buyers",
          ).then(res=>{
              commit("listOfBuyers",res.data)}
        )
    },
    
     /*
        ###################################################################
    */
    // Liste de tous les travaux fait par un buyers
    async region({commit}){
        await axios.get(
            "http://localhost:8000/api/regions")
            .then(res=>{
                commit("getRegion",res.data)
            })
    },
    /*
        ###################################################################
    */
    
     /*
        ###################################################################
    */
    // Liste de tous les travaux fait par un buyers
    async recordsDone({commit},id){
        await axios.get(
            `http://localhost:8000/api/buyers/${id}/records/done/`)
            .then(res=>{
                commit("listRecordsDone",res.data)
            })
    },
    /*
        ###################################################################
    */


     /*
        ###################################################################
    */
    // Une region en particulier
    async oneRegion({commit},id){
        await axios.get(
            `http://localhost:8000/api/regions/${id}/records`)
            .then(res=>{
                commit("particularRegion",res.data)
            })
    },
    
    /*
        ###################################################################
    */
    // Liste de tous les travaux en cours par buyers
    async recordsInprogress({commit},id){
        await axios.get(
            `http://localhost:8000/api/buyers/${id}/records/in_progress/`)
            .then(res=>{
                commit("listRecordsInprogress",res.data)
        })
    },
    async records({commit},id){
        await axios.get(
            `http://localhost:8000/api/buyers/${id}/records/`)
            .then(res=>{
                commit("listOfRecords",res.data)
        })
    },


    async allRecordsInprogress({commit}){
        await axios.get(
            `http://localhost:8000/api/buyers/records/in_progress/`)
            .then(res=>{
                commit("listRecordsInprogress",res.data)
        })
    },

    /*
        ###################################################################
    */
    // Liste de tous les totaux encore et terminé par buyers
    async tendersBuyer({commit},id){
        await axios.get(
            `http://localhost:8000/api/buyers/${id}/records/total`)
            .then(res=>{
                commit("listTotauxBuyer",res.data)
        })
    },
    /*
        ###################################################################
    */
    // Liste de tous les specification
    async specification({commit}){
        await axios.get(
            `http://localhost:8000/api/records`)
            .then(res=>{
                commit("listSpecification",res.data)
        })
    },
    /*
        ###################################################################
    */
    // Liste de tous les marchés et leurs etats
    async tendersByYear({commit},year){
        await axios.get(
            `http://localhost:8000/api/tenders/year/${year}/tender_state`)
            .then(res=>{
                commit("listTendersByYear",res.data)
        })
    },

    /*
        ###################################################################
    */
    // Liste de tous les buyers par regions
    async buyerByRegion({commit},year){
        await axios.get(
            `http://localhost:8000/api/buyers/${year}/total_by_region`)
            .then(res=>{
                commit("listBuyerByRegion",res.data)
        })
    },
    

}
export const getters = {}




// Colaboration : 
// etude : doc,url