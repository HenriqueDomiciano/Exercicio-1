<template>
  <div id = 'app' class="covid">
    <h1 class = 'main header mt-5' style="text-align:center">Covid vaccination worldwide</h1>
      <div class="select mt-5" style="text-align:center">
        <select style ="text-align:center" v-model="selected" v-on:click='see(selected)'>
        <option  class="option" disabled value="">Chose an item</option>
        <option class = 'option'>ISO</option>
        <option class = 'option'>NAME</option>
        </select>
      </div>
    <div class="iso mt-2" v-show="is_ISO" style="text-align:center">    
      <input class='value' v-model.trim="input_iso" placeholder = 'Put the country ISO code with 3 letters'>
      <input class='button' type = 'Submit' value = 'Submit' v-on:click= 'search("ISO")'>
    </div>
    <div class="name mt-2" v-show='is_name' style="text-align:center">
      <input class='value' v-model.trim="input_name" placeholder = 'Put the country name'>
      <input class ='button' type = 'Submit' value = 'Submit' v-on:click= 'search("name")'>
    </div>
    <div class='graphs' id = 'graphs' v-if="loaded">
      <div class="firstchart">
        <div class="row mt-5">
          <div class="col">
            <h2 style="text-align:center">Daily Applied Vaccines of {{country}}</h2>
            <line-chart :chartData='new_daily_vac' :secondData="[]" :options='chart_options' label = 'Vaccines aplied daily' label2=''></line-chart>
          </div>
        </div>
      <div class="second">
        <div class="row mt-5">
          <div class="col">
            <h2 style="text-align:center">Applied Vaccines of {{country}}</h2>
            <line-chart :chartData='arrvacination_total' :secondData='[]' :options='chart_options' label = 'total Vaccinations' label2=''></line-chart>
          </div>
        </div>
      </div>
      <div class="third" >
        <div class="row mt-5">
          <div class="col">
            <h2 style="text-align:center">People Vaccinated {{country}}</h2>
            <line-chart :chartData='arrpeoplevaccinated' :secondData="arrpeople_fully_vaccinated" :options='chart_options' label = 'People vaccinated with at least one dose' label2 = 'people fully vaccinated'></line-chart>
          </div>
        </div>
      <div class="fourth">
        <div class="row mt-5">
          <div class="col">
            <h2 style="text-align:center">People Vaccinated per 100 people of {{country}}</h2>
            <line-chart :chartData='arrvacination_per_hundred' :secondData="arrfully_vaccinated_per_hundred" :options='chart_options' label = 'People vaccinated with at least one dose/100 people ' label2 = 'people fully vaccinated/100 people '></line-chart>
          </div>
        </div>
      </div>
      <div class="fifth">
        <div class="row mt-5">
          <div class="col">
            <h2 style="text-align:center">Number of cases of covid-19 Daily of {{country}}</h2>
            <line-chart :chartData='arrnew_cases_covid' :secondData="[]" :options='chart_options' label = 'Number of new cases' label2 = ''></line-chart>
          </div>
        </div>
      </div>
      <div class="six">
        <div class="row mt-5">
          <div class="col">
            <h2 style="text-align:center">Number of deaths by covid-19 Daily of {{country}}</h2>
            <line-chart :chartData='arrnew_deaths_covid' :secondData="[]" :options='chart_options' label = 'Number of Deaths by covid-19' label2 = ''></line-chart>
          </div>
        </div>
      </div>
      <div class="seven">
        <div class="row mt-5">
          <div class="col">
            <h2 style="text-align:center">Reproduction rate of covid 19 in {{country}}</h2>
            <line-chart :chartData='arrconst' :secondData="[]" :options='chart_options' label = 'Reproduction rate' label2 = ''></line-chart>
          </div>
        </div>
      </div>
      <div class="eigth">
        <div class="row mt-5">
          <div class="col">
            <h2 style="text-align:center">Acumulated cases of covid-19 in {{country}}</h2>
            <line-chart :chartData='arrcases_covid' :secondData="[]" :options='chart_options' label = 'Accumulated cases of covid-19' label2 = ''></line-chart>
          </div>
        </div>
      </div>
      <div class="nine">
        <div class="row mt-5">
          <div class="col">
            <h2 style="text-align:center">Number of deaths by covid-19 in {{country}}</h2>
            <line-chart :chartData='arrdeaths_covid' :secondData="[]" :options='chart_options' label = 'Number of deaths by covid-19' label2 = ''></line-chart>
          </div>
        </div>
      </div>
      <div class="ten">
        <div class="row mt-5">
          <div class="col">
            <h2 style="text-align:center">Number of tests applied in that day in {{country}}</h2>
            <line-chart :chartData='arrnew_test' :secondData="[]" :options='chart_options' label = 'New tests of covid-19' label2 = ''></line-chart>
          </div>
        </div>
      </div>
      <div class="eleven">
        <div class="row mt-5">
          <div class="col">
            <h2 style="text-align:center">Number of accumulated tests of covid-19 in {{country}}</h2>
            <line-chart :chartData='arrtests' :secondData="[]" :options='chart_options' label = 'Accumulated tests' label2 = ''></line-chart>
          </div>
        </div>
      </div>
    </div>
      <div class="vaccines mt-5" style="text-align:center">
        <p>The vaccine(s) used in {{country}} are</p>
        <p>{{vaccines}}</p>
      </div>
      <div class="font" style="text-align:center">
        <p>This data can be found on <a v-bind:href ='font' target="_blank">{{font}}</a></p>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import LineChart from './components/LineChart.vue'
import axios from 'axios'
import moment from 'moment'
export default {
  name: 'App',
  components: {
    LineChart
  },
  data () {
    return {
      loaded : false,
      is_ISO : false,
      is_name: false,
      vaccines:'',
      datacases:[],
      
      new_daily_vac:[],
      arrpeoplevaccinated:[],
      arrpeople_fully_vaccinated: [],
      arrvacination_daily : [],
      arrvacination_total : [],
      arrvacination_per_hundred:[],
      arrfully_vaccinated_per_hundred:[],

      arrnew_cases_covid:[],
      arrnew_deaths_covid:[],
      arrcases_covid : [],
      arrdeaths_covid: [],
      arrconst:[],
      arrtests:[],
      arrnew_test:[],

      input_iso : '',
      input_name:'',
      ISO:'',
      country :'',
      font:'',
      chart_options:{
        responsive : true,
        maintainAspectRatio : false
      }
    }
  },
  methods:{
    async search(name) {
      const client = axios.create({
        auth: {
          username: "admin",  
          password: "suadmin"
        },
        headers: {
          "Content-Type": "application/json"
        }
      });
      this.loaded=false
      this.new_daily_vac = []
      this.arrvacination_daily = []
      this.arrvacination_total = []
      this.arrvacination_per_hundred = []
      this.arrpeople_fully_vaccinated = []
      this.arrpeoplevaccinated = []
      this.arrfully_vaccinated_per_hundred = []
      this.vaccines = ''
      this.font = ''
      this.name =''
      this.ISO = ''
      this.arrnew_cases_covid=[]
      this.arrconst=[]
      this.arrnew_deaths_covid=[]
      this.arrcases_covid=[]
      this.arrdeaths_covid=[]
      this.arrnew_test=[]
      this.arrtests=[]
      if (this.input_iso.length==3 || this.input_name.length>=3){
        this.ISO = this.input_iso.toUpperCase()
        this.name = this.input_name.charAt(0).toUpperCase() + this.input_name.slice(1)
        if(name=='name'){
          var adress = this.name
        }
        else{
          var adress = this.ISO
        } 
        const {data} = await client.get('http://127.0.0.1:5000/Country?'+ name +'='+ adress +'&is_vaccine=vaccines');
        data.forEach(d=>{
          const date = moment(d.date,"YYYY-MM-DD").format('DD/MM/YYYY')
          const {
              country,
              iso_code,
              total_vaccinations,
              people_vaccinated,
              people_fully_vaccinated,
              daily_vaccinations_raw,
              daily_vaccinations,
              people_vaccinated_per_hundred,
              people_fully_vaccinated_per_hundred,
              vaccines,
              source_website
          } = d;
          this.ISO = iso_code
          this.country = country
          this.new_daily_vac.push({date,total:daily_vaccinations}) 
          this.arrvacination_daily.push({date,total:daily_vaccinations_raw})
          this.arrpeople_fully_vaccinated.push({date,total:people_fully_vaccinated})
          this.arrvacination_per_hundred.push({date,total:people_vaccinated_per_hundred})
          this.arrvacination_total.push({date,total:total_vaccinations})
          this.arrpeoplevaccinated.push({date,total:people_vaccinated})
          this.arrfully_vaccinated_per_hundred.push({date,total:people_fully_vaccinated_per_hundred})
          this.vaccines=vaccines
          this.font=source_website
        })
      
      
      await client.get('http://127.0.0.1:5000/Country?ISO='+ this.ISO +'&is_vaccine=cases').then(
        response=>(this.datacases=response.data)
      )
      this.datacases.forEach(d=>{
        const date = moment(d.date,'MM/DD/YYYY').format('DD/MM/YYYY')
        const{
          total_cases,
          new_cases,
          total_deaths,
          new_deaths,
          reproduction_rate,
          new_tests,
          total_tests
        }=d;
        this.arrnew_cases_covid.push({date,total:new_cases})
        this.arrnew_deaths_covid.push({date,total:new_deaths})
        this.arrconst.push({date,total:reproduction_rate})
        this.arrcases_covid.push({date,total:total_cases})
        this.arrdeaths_covid.push({date,total:total_deaths})
        this.arrtests.push({date,total:total_tests})
        this.arrnew_test.push({date,total:new_tests})
        this.loaded=true
      })
      }
      
      
      
      
      
      else{
        alert("Not a valid ISO or Name")  
      }
    },




    see: function(value){
      if (value=='ISO'){
        this.is_ISO=true
        this.is_name=false
      }
      else{
        this.is_ISO=false
        this.is_name=true
      }
    },
  
  
  }


}
</script>

<style>
.value{
  background-color:rgb(158, 154, 138);
  border-color: rgb(158, 154, 138) ;
  border-radius: 10px;
  padding-right: 20px;
  padding-left:20px;
}
.option{
  background-color:rgb(158, 154, 138);
  border-color:rgb(158, 154, 138);
}
.button{
  border-color:rgb(158, 154, 138) ;
  background-color:rgb(158, 154, 138);
  border-radius:10px;
  margin-left: 5px;
}

</style>