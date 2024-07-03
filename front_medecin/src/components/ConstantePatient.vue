<script>
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js'
import PrimaryButton from '@/components/PrimaryButton.vue';
import { data } from 'autoprefixer';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, PointElement, LineElement)


export default {
  components: {
    PrimaryButton,
    Line
  },
  props:{
    constantes: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      chartOptions: {
        responsive: true
      },
      page: 1,
      choixConstante: ["frequence_cardiaque", "tension", "temperature"]
    }
  },
  computed: {
    chartData() {
      return {
        labels: this.constantes.map(element => element.date_releve),
        datasets: [{
          label: 'My First Dataset',
          data: this.constantes.map(element => {
            if (this.page == 1){ return element.frequence_cardiaque; }
            if (this.page == 2){ return element.tension; }
            if (this.page == 3){ return element.temperature; }
          }),
          fill: false,
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.01
        }]      
      }  
    }
  },
  methods: {
    navBarre(index){
      this.page = index;
    }
  }
};
</script>

<template>
  <BaseLayout>
    <div class="grid h-full grid-cols-5 gap-2">
        
      <div class="col-span-1 row-span-2 px-2 bg-white rounded-md">
        <div v-if="constantes!=undefined || constantes!=null" class="rounded-3xl h-fit">
          <div class="flex flex-col w-full gap-2 h-fit">
            <span class="font-semibold text-center underline">Dernière constante</span>
            <p>Date : <span>{{ constantes[constantes.length-1].date_releve }}</span></p>
            <p>Fréquence cardiaque : <span>{{ constantes[constantes.length-1].frequence_cardiaque }}</span></p>
            <p>Température : <span>{{ constantes[constantes.length-1].temperature }}</span></p>
            <p>Tension : <span>{{ constantes[constantes.length-1].tension }}</span></p>
            <p>Poids : <span>{{ constantes[constantes.length-1].poids }}</span> kg</p>
            <p>Taille : <span>{{ constantes[constantes.length-1].taille }}</span> cm</p>
            <p>IMC : <span>{{ (constantes[constantes.length-1].taille/constantes[constantes.length-1].poids)*constantes[constantes.length-1].poids }}</span></p>
            <p>Groupe sanguiun : <span>{{ constantes[constantes.length-1].groupe_sanguin }}</span></p>
          </div>
        </div>
      </div>
    
      <div class="col-span-4 row-span-5 p-2 overflow-hidden bg-white rounded-md bg-gradient-to-tr">
        <div class="flex items-end justify-between">
          <PrimaryButton class="h-fit mx-0.5" @click="navBarre(1)" :buttonClass="{'bg-mercury-200 bg-image-none text-black shadow-none':page!=1, 'text-white':page==1}">Fréquence cardiaque</PrimaryButton>
          <PrimaryButton class="h-fit mx-0.5" @click="navBarre(2)" :buttonClass="{'bg-mercury-200 bg-image-none text-black shadow-none':page!=2, 'text-white':page==2}">Tension</PrimaryButton>
          <PrimaryButton class="h-fit mx-0.5" @click="navBarre(3)" :buttonClass="{'bg-mercury-200 bg-image-none text-black shadow-none':page!=3, 'text-white':page==3}">Température</PrimaryButton>
        </div>
        <div class="flex flex-col h-full gap-4 p-2 overflow-auto">
          <Line id="my-chart-id" :options="chartOptions" :data="chartData"/>
        </div>
      </div>

      <div class="col-span-1 row-span-3 p-2 bg-white rounded-md">
        <div class="flex flex-col w-full rounded-3xl">
          <span class="font-semibold text-center underline">Nouvelle constante</span>
          <PrimaryButton v-for="(examen, index) in examens" :key="index" class='mb-2'>{{ examen.date }} <br> {{ examen.motif }}</PrimaryButton>
        </div>
      </div>

      

    </div>
  </BaseLayout>
</template>
