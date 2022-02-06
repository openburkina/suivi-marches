import axios from 'axios'
import { pieStatAdapter, lineStatAdapter, barStatAdapter } from '~/helpers/Adapters'

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
    recordsTotalOfBuyeur:[],
    idRegion: 0,
    statasList: [],
    tmpStat:{},
    homePieStats: {'labels': [], 'data': []},
    homeBarOneStats: {'labels': [], 'data': []},
    homeBarTwoStats: {'labels': [], 'data': []},
    homeLineStats: {'labels': [], 'data': []},
    regionPieStats: {'labels': [], 'data': []},
    regionBarOneStats: {'labels': [], 'data': []},
    regionBarTwoStats: {'labels': [], 'data': []},
    regionLineStats: {'labels': [], 'data': []},
    buyerPieStats: {'labels': [], 'data': []},
    buyerBarOneStats: {'labels': [], 'data': []},
    buyerBarTwoStats: {'labels': [], 'data': []},
    buyerLineStats: {'labels': [], 'data': []}
  })

export const mutations = {
    setHomePieStats(state, payload) {
        state.homePieStats = payload.data
    },
    setHomeBarOneStats(state, payload) {
        state.homeBarOneStats = payload.data
    },
    setHomeBarTwoStats(state, payload) {
        state.homeBarTwoStats = payload.data
    },
    setHomeLineStats(state, payload) {
        state.homeLineStats = payload.data
    },

    setRegionPieStats(state, payload) {
        state.regionPieStats = payload.data
    },
    setRegionBarOneStats(state, payload) {
        state.regionBarOneStats = payload.data
    },
    setRegionBarTwoStats(state, payload) {
        state.regionBarTwoStats = payload.data
    },
    setRegionLineStats(state, payload) {
        state.regionLineStats = payload.data
    },

    setBuyerPieStats(state, payload) {
        state.buyerPieStats = payload.data
    },
    setBuyerBarOneStats(state, payload) {
        state.buyerBarOneStats = payload.data
    },
    setBuyerBarTwoStats(state, payload) {
        state.buyerBarTwoStats = payload.data
    },
    setBuyerLineStats(state, payload) {
        state.buyerLineStats = payload.data
    },


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
    // setter de liste total d'un records pour un buyeur
    recordsTotalBuyeur(state,paylaod){
        state.recordsTotalOfBuyeur = paylaod
        console.log(state.recordsTotalOfBuyeur)

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

    },

    
    statasBuyer(state,paylaod){
        state.tmpStat = paylaod
        state.tmpList.push(state.tmpStat.Finish)
        state.tmpList.push(state.tmpStat.In_progress)
        state.tmpStat = {}
        state.statasList = state.tmpList
        state.tmpList = []

    }

}
export const actions = {

    // Home Stats
    async fetchHomePieStats({ commit }, { year }) {
        await axios.get(
            `http://localhost:8000/api/records/by_status?year=${year}`
        ).then(res => {
            commit("setHomePieStats", {name: "pie", data : pieStatAdapter(res.data)})
        })
    },
    async fetchHomeBarOneStats({ commit }, { year }) {
        axios.get(
            `http://localhost:8000/api/records/values?group_by=region&year=${year}`
        ).then(res => {
            commit("setHomeBarOneStats", {name: "barOne", data : barStatAdapter(res.data)})
        })
    },
    async fetchHomeBarTwoStats({ commit }, { year }) {
        axios.get(
            `http://localhost:8000/api/records/values?group_by=sector&year=${year}`
        ).then(res => {
            commit("setHomeBarTwoStats", {name: "barTwo", data : barStatAdapter(res.data)})
        })
    },
    async fetchHomeLineStats({ commit }, { start_year, end_year }) {
        await axios.get(
            `http://localhost:8000/api/records/sector_values?start_year=${start_year}&end_year=${end_year}`
        ).then(res => {
            commit("setHomeLineStats", {name: "line", data : lineStatAdapter(res.data, start_year, end_year)})
        })
    },
    // End Home Stats
    
    // Region Stats
    async fetchRegionPieStats({ commit }, { country, region, year }) {
        await axios.get(
            `http://localhost:8000/api/regions/records/by_status?country=${country}&region=${region}&year=${year}`
        ).then(res => {
            commit("setRegionPieStats", {name: "pie", data : pieStatAdapter(res.data)})
        })
    },
    async fetchRegionBarOneStats({ commit }, { country, region, year }) {
        axios.get(
            `http://localhost:8000/api/regions/records/values?country=${country}&region=${region}&group_by=buyer&year=${year}`
        ).then(res => {
            commit("setRegionBarOneStats", {name: "barOne", data : barStatAdapter(res.data)})
        })
    },
    async fetchRegionBarTwoStats({ commit }, { country, region, year }) {
        axios.get(
            `http://localhost:8000/api/regions/records/values?country=${country}&region=${region}&group_by=sector&year=${year}`
        ).then(res => {
            commit("setRegionBarTwoStats", {name: "barTwo", data : barStatAdapter(res.data)})
        })
    },
    async fetchRegionLineStats({ commit }, { country, region, start_year, end_year }) {
        await axios.get(
            `http://localhost:8000/api/regions/records/sector_values?country=${country}&region=${region}&start_year=${start_year}&end_year=${end_year}`
        ).then(res => {
            commit("setRegionLineStats", {name: "line", data : lineStatAdapter(res.data, start_year, end_year)})
        })
    },
    // End Region Stats
    
    // Buyer Stats
    async fetchBuyerPieStats({ commit }, { buyer_id, year }) {
        await axios.get(
            `http://localhost:8000/api/buyers/${buyer_id}/records/by_status?year=${year}`
        ).then(res => {
            commit("setBuyerPieStats", {name: "pie", data : pieStatAdapter(res.data)})
        })
    },
    async fetchBuyerBarOneStats({ commit }, { buyer_id, year }) {
        axios.get(
            `http://localhost:8000/api/buyers/${buyer_id}/records/values?group_by=region&year=${year}`
        ).then(res => {
            commit("setBuyerBarOneStats", {name: "barOne", data : barStatAdapter(res.data)})
        })
    },
    async fetchBuyerBarTwoStats({ commit }, { buyer_id, year }) {
        axios.get(
            `http://localhost:8000/api/buyers/${buyer_id}/records/values?group_by=sector&year=${year}`
        ).then(res => {
            commit("setBuyerBarTwoStats", {name: "barTwo", data : barStatAdapter(res.data)})
        })
    },
    async fetchBuyerLineStats({ commit }, { buyer_id, start_year, end_year }) {
        await axios.get(
            `http://localhost:8000/api/buyers/${buyer_id}/records/sector_values?start_year=${start_year}&end_year=${end_year}`
        ).then(res => {
            commit("setBuyerLineStats", {name: "line", data : lineStatAdapter(res.data, start_year, end_year)})
        })
    },
    // End Buyer Stats

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
    // Liste de tous les buyers
    async recordsTotalByBuyeur({ commit },id){
       
        await axios.get(
            `http://localhost:8000/api/buyers/${id}/records/total/`,
          ).then(res=>{
              commit("recordsTotalBuyeur",res.data)}
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
    async oneRegion({commit}, {country, region}){
        await axios.get(
            `http://localhost:8000/api/regions/records?country=${country}&region=${region}`)
            .then(res=>{
                commit("particularRegion",res.data)
            })
    },

    /*
        ###################################################################
    */
    // Une region en particulier
    async statasOfBuyer({commit},id){
        await axios.get(
            `http://localhost:8000/api/buyers/${id}/total/`)
            .then(res=>{
                commit("statasBuyer",res.data)
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
        });
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