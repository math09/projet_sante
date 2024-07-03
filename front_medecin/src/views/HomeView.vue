<script>
import BaseLayout from '@/layouts/BaseLayout.vue';
import PrimaryButton from '@/components/PrimaryButton.vue';
import ListPatient from '@/components/ListPatient.vue';
import InfoPatient from '@/components/InfoPatient.vue';
import ExamensPatient from '@/components/ExamensPatient.vue';
import ConstantePatient from '@/components/ConstantePatient.vue';
import PrescriptionPatient from '@/components/PrescriptionPatient.vue';
import axios from '@/utils/axiosInterseptor'

export default {
  name: 'HomeView',
  components: {
    BaseLayout,
    PrimaryButton,
    ListPatient,
    InfoPatient,
    ExamensPatient,
    ConstantePatient,
    PrescriptionPatient
  },
  data() {
    return {
      persons: [],
      examens: [],
      constantes: [],
      prescriptions: [],
      medicaments: [],
      patientAffiche: null,
      page: 1
    };
  },
  methods: {
    navBarre(index){
      this.page = index;
    },
    onPatientSelected(index){
      this.patientAffiche=index;
    },
    async submitExam(data){
      await axios.post("examens", {
        motif: data.motif,
        diagnostic: data.diagnostic,
        resultat_analyse: data.analyse,
        conclusion: data.conclusion,
        observation: data.observation,
        id_patient: this.patientAffiche,
        date_examen: "2023-07-03",
        id_medecin: 1
      }).then((response) => {
        this.examens.push(response.data);
      });
    },
    async submitConstante(data){
      let values = {
        frequence_cardiaque: null,
        tension: null,
        temperature: null,
        groupe_sanguin: null,
        poids: null,
        taille: null,
        id_patient: this.patientAffiche
      }

      switch (data.type) {
        case "1":
          values.frequence_cardiaque = data.value
          break;
        case "2":
          values.tension = data.value
          break;
        case "3":
          values.temperature = data.value
          break;
        case "4":
          values.poids = data.value
          break;
        case "5":
          values.taille = data.value
          break;
        case "6":
          values.groupe_sanguin = data.value
          break;
        default:
          break;
      }

      await axios.post('constantes', values).then((res) => {
        console.log(res.data);
        this.constantes.push(res.data);
      });

      // await axios.get('constantes').then((response) => {
      //   this.constantes = response.data;
      // });
    }
  },
  async mounted(){
    await axios.get('patients').then((response) => {
      this.persons = response.data;
    });

    await axios.get('examens').then((response) => {
      this.examens = response.data;
    });

    await axios.get('constantes').then((response) => {
      this.constantes = response.data;
    });

    await axios.get('prescriptions').then((response) => {
      this.prescriptions = response.data;
    });

    await axios.get('medicaments').then((response) => {
      this.medicaments = response.data;
    });
  },
  computed:{
    getLastConstante(){
      const lastConstante = this.constantes.filter(constante => constante.id_patient==this.patientAffiche)
      if(lastConstante.length==0){
        return null;
      }else{
        return lastConstante[lastConstante.length -1];
      }
    }
  }
};
</script>

<template>
  <BaseLayout> 
    <div class="grid h-full grid-cols-5 gap-6">
      <div class="flex-grow col">
        <ListPatient :persons="persons" @person_selected="onPatientSelected"/>
      </div>

      <div class="col-span-4 overflow-hidden bg-gradient-to-tr">
        <div class="relative flex flex-col h-full gap-4 p-4 rounded-md bg-mercury-200">
          
          <div class="flex items-end justify-between gap-2">
            <PrimaryButton :disabled="!patientAffiche" class="h-fit" @click="navBarre(1)" :buttonClass="{'bg-white bg-image-none text-black':page!=1, 'text-white':page==1}">Informations patient</PrimaryButton>
            <PrimaryButton :disabled="!patientAffiche" class="h-fit" @click="navBarre(2)" :buttonClass="{'bg-white bg-image-none text-black':page!=2, 'text-white':page==2}">Examens</PrimaryButton>
            <PrimaryButton :disabled="!patientAffiche" class="h-fit" @click="navBarre(3)" :buttonClass="{'bg-white bg-image-none text-black':page!=3, 'text-white':page==3}">Constante</PrimaryButton>
            <PrimaryButton :disabled="!patientAffiche" class="h-fit" @click="navBarre(4)" :buttonClass="{'bg-white bg-image-none text-black':page!=4, 'text-white':page==4}">Prescription</PrimaryButton>
          </div>

          <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-Y-1/2" v-if="!patientAffiche">
              <p class=" text-xl font-semibold">Veuillez sélectionner un patient</p>
          </div>
          
          <div v-if="page==1 && persons!=undefined" class="h-full">
            <InfoPatient :person="persons.find(person => person.num_secu==patientAffiche)" :constante="getLastConstante"/>
          </div>

          <div v-if="page==2 && examens!=undefined" class="h-full">
            <ExamensPatient :examens="examens.filter(examen => examen.id_patient==patientAffiche)" @submit_exam="submitExam"/>
          </div>

          <div v-if="page==3 && constantes!=undefined" class="h-full">
            <ConstantePatient :constantes="constantes.filter(constante => constante.id_patient==patientAffiche)" @submit_constante="submitConstante"/>
          </div>

          <div v-if="page==4 && medicaments!=undefined" class="h-full">
            <PrescriptionPatient :medicaments="medicaments"/>
          </div>
          
        </div>
      </div>

    </div>


  </BaseLayout>
</template>
