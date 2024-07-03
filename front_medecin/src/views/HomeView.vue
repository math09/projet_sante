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
      persons: null,
      examens: null,
      constantes: null,
      prescriptions: null,
      medicaments: null,
      patientAffiche: 5,
      page: 4
    };
  },
  methods: {
    navBarre(index){
      this.page = index;
    },
    onPatientSelected(index){
      this.patientAffiche=index;
    }
  },
  async mounted(){
    this.persons = try {
          await axios.get('/api/patients').then((response) => { 
          console.log('api response :'+response);
          return response.data})}
          catch (e) {
          console.log("api don't response\n"+e); 
          return ( [
        { id: 1, nom: "JEAN", prenom: "Anthony", date_naissance: "06/06/1986", lieu_de_naissance: "Lyon", 
        num_secu: "1 03 000 000 0000", num_mutuelle: "0123456789", nom_mutuelle: "Patrick", 
        adresse: "01 rue de Lyon", etat: "", pays: "France", 
        num_telephone: "0606060606", email: "test.test@pmail.com", 
        personneAContacter: {nom_contact: "JEAN", prenom_contact: "Anthony", num_contact: "0707070707"}, 
        autre: {antecedent: "Braquage a main armée", allergie: "Cuivre"} },
        { id: 2, nom: "SMITH", prenom: "John", date_naissance: "06/06/1986", lieu_de_naissance: "Lyon", 
        num_secu: "1 03 000 000 0000", num_mutuelle: "0123456789", nom_mutuelle: "Patrick", 
        adresse: "01 rue de Lyon", etat: "", pays: "France", 
        num_telephone: "0606060606", email: "test.test@pmail.com", 
        personneAContacter: {nom_contact: "JEAN", prenom_contact: "Anthony", num_contact: "0707070707"}, 
        autre: {antecedent: "Braquage a main armée", allergie: "Cuivre"} },
        { id: 3, nom: "PEYRARD", prenom: "Thibaut", date_naissance: "06/06/1986", lieu_de_naissance: "Lyon", 
        num_secu: "1 03 000 000 0000", num_mutuelle: "0123456789", nom_mutuelle: "Patrick", 
        adresse: "01 rue de Lyon", etat: "", pays: "France", 
        num_telephone: "0606060606", email: "test.test@pmail.com", 
        personneAContacter: {nom_contact: "JEAN", prenom_contact: "Anthony", num_contact: "0707070707"}, 
        autre: {antecedent: "Braquage a main armée", allergie: "Cuivre"} },
        { id: 4, nom: "JOHN", prenom: "Smith", date_naissance: "06/06/1986", lieu_de_naissance: "Lyon", 
        num_secu: "1 03 000 000 0000", num_mutuelle: "0123456789", nom_mutuelle: "Patrick", 
        adresse: "01 rue de Lyon", etat: "", pays: "France", 
        num_telephone: "0606060606", email: "test.test@pmail.com", 
        personneAContacter: {nom_contact: "JEAN", prenom_contact: "Anthony", num_contact: "0707070707"}, 
        autre: {antecedent: "Braquage a main armée", allergie: "Cuivre"} },
        { id: 5, nom: "TEST", prenom: "Test", date_naissance: "06/06/1986", lieu_de_naissance: "Lyon", 
        num_secu: "1 03 000 000 0000", num_mutuelle: "0123456789", nom_mutuelle: "Patrick", 
        adresse: "01 rue de Lyon", etat: "", pays: "France", 
        num_telephone: "0606060606", email: "test.test@pmail.com", 
        personneAContacter: {nom_contact: "JEAN", prenom_contact: "Anthony", num_contact: "0707070707"}, 
        autre: {antecedent: "Braquage a main armée", allergie: "Cuivre"} },
      ])},
    this.examens = await axios.get('/api/examens').then((response) => { 
        if (response!=null || response!=undefined){ console.log('api response :'+response); return response.data} 
        else {console.log("api don't response"); 
        return ( [
      {id_examen: "5", id_patient: "1", motif: "Respire en lieu public", observation: "Ses poumons ont besoin d'air", 
      diagnostic: "Prescription de médicament anti-respiration", resultat_analyse: "Respire", conclusion: "Doit arreter de respirer",
      date: "11/11/1111 11:11:11.111" },
      {id_examen: "4", id_patient: "2", motif: "Respire en lieu public", observation: "Ses poumons ont besoin d'air", 
      diagnostic: "Prescription de médicament anti-respiration", resultat_analyse: "Respire", conclusion: "Doit arreter de respirer",
      date: "22/22/2222 22:22:22.222" },
      {id_examen: "3", id_patient: "3", motif: "Respire en lieu public", observation: "Ses poumons ont besoin d'air", 
      diagnostic: "Prescription de médicament anti-respiration", resultat_analyse: "Respire", conclusion: "Doit arreter de respirer",
      date: "33/33/3333 33:33:33.333" },
      {id_examen: "2", id_patient: "4", motif: "Respire en lieu public", observation: "Ses poumons ont besoin d'air", 
      diagnostic: "Prescription de médicament anti-respiration", resultat_analyse: "Respire", conclusion: "Doit arreter de respirer",
      date: "44/44/4444 44:44:44.444" },
      {id_examen: "1", id_patient: "5", motif: "Respire en lieu public", observation: "Ses poumons ont besoin d'air", 
      diagnostic: "Prescription de médicament anti-respiration", resultat_analyse: "Respire", conclusion: "Doit arreter de respirer",
      date: "55/55/5555 55:55:55.555" }
    ])}}),
    this.constantes = async () => {
        await axios.get('/api/patients').then((response) => { 
          if (response!=null || response!=undefined){ console.log('api response :'+response); return response.data} 
          else {console.log("api don't response"); 
          return ( [
        { id_constante: "1", id_patient: "5", frequence_cardiaque: "12", tension: "2", temperature: "37", groupe_sanguin: "O+", poids: "90", taille: "90", date_releve: "55/55/5555" },
        { id_constante: "2", id_patient: "4", frequence_cardiaque: "14", tension: "2", temperature: "37", groupe_sanguin: "O+", poids: "90", taille: "90", date_releve: "44/44/4444" },
        { id_constante: "5", id_patient: "3", frequence_cardiaque: "16", tension: "2", temperature: "37", groupe_sanguin: "O+", poids: "90", taille: "90", date_releve: "33/33/3333" },
        { id_constante: "3", id_patient: "2", frequence_cardiaque: "19", tension: "2", temperature: "37", groupe_sanguin: "O+", poids: "90", taille: "90", date_releve: "22/22/2222" },
        { id_constante: "4", id_patient: "1", frequence_cardiaque: "10", tension: "2", temperature: "37", groupe_sanguin: "O+", poids: "90", taille: "90", date_releve: "11/11/1111" }
      ])}})
    },
    this.prescriptions = async () => {
      await axios.get('/api/examens').then((response) => { 
        if (response!=null || response!=undefined){ console.log('api response :'+response); return response.data} 
        else {console.log("api don't response"); 
        return ( [
        { id_medicament: "1", id_patient: "1", date_debut: "55/55/5555", date_fin: "55/55/5556", periodicite: "0.5 fois par jour", medicaments: "Advil", champs_libre: "Je suis libre", signature: "1234" },
        { id_medicament: "2", id_patient: "3", date_debut: "22/22/2222", date_fin: "22/22/2223", periodicite: "0.5 fois par jour", medicaments: "Advil", champs_libre: "Je suis libre", signature: "1234" },
        { id_medicament: "3", id_patient: "4", date_debut: "33/33/3333", date_fin: "33/33/3334", periodicite: "0.5 fois par jour", medicaments: "Advil", champs_libre: "Je suis libre", signature: "1234" },
        { id_medicament: "4", id_patient: "2", date_debut: "11/11/1111", date_fin: "11/11/1112", periodicite: "0.5 fois par jour", medicaments: "Advil", champs_libre: "Je suis libre", signature: "1234" }
      ] )}})
    },
    this.medicaments = async () => {
      await axios.get('/api/examens').then((response) => { 
        if (response!=null || response!=undefined){ console.log('api response :'+response); return response.data} 
        else {console.log("api don't response"); 
        return ( [
          {nom_medicament: "Paracétamol", ref_medicament: "1", molecule: "C8H9NO2"},
          {nom_medicament: "Ibuprofène", ref_medicament: "2", molecule: "C13H18O2"},
          {nom_medicament: "Alginate de sodium", ref_medicament: "3", molecule: "(C₆H₇NaO₆)n"},
          {nom_medicament: "Cétylpyridinium chlorure", ref_medicament: "4", molecule: "	C21H38CiN"}
        ] )}})
    }
    console.log('this.persons');
    console.log(this.persons);
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
        <div class="flex flex-col h-full gap-4 p-4 rounded-md bg-mercury-200">
          
          <div class="flex items-end justify-between">
            <PrimaryButton class="h-fit mx-0.5" @click="navBarre(1)" :buttonClass="{'bg-white bg-image-none text-black':page!=1, 'text-white':page==1}">Informations patient</PrimaryButton>
            <PrimaryButton class="h-fit mx-0.5" @click="navBarre(2)" :buttonClass="{'bg-white bg-image-none text-black':page!=2, 'text-white':page==2}">Examens</PrimaryButton>
            <PrimaryButton class="h-fit mx-0.5" @click="navBarre(3)" :buttonClass="{'bg-white bg-image-none text-black':page!=3, 'text-white':page==3}">Constante</PrimaryButton>
            <PrimaryButton class="h-fit mx-0.5" @click="navBarre(4)" :buttonClass="{'bg-white bg-image-none text-black':page!=4, 'text-white':page==4}">Prescription</PrimaryButton>
          </div>
          
          <div v-if="page==1 || persons!=undefined" class="h-full">
            <InfoPatient :person="persons.find(person => person.id==patientAffiche)"/>
          </div>

          <div v-if="page==2 || examens!=undefined" class="h-full">
            <ExamensPatient :examens="examens.filter(examen => examen.id_patient==patientAffiche)"/>
          </div>

          <div v-if="page==3 || constantes!=undefined" class="h-full">
            <ConstantePatient :constantes="constantes.filter(constante => constante.id_patient==patientAffiche)"/>
          </div>

          <div v-if="page==4 || medicaments!=undefined" class="h-full">
            <PrescriptionPatient :medicaments="medicaments"/>
          </div>
          
        </div>
      </div>

    </div>


  </BaseLayout>
</template>
