<script>
import BaseLayout from '@/layouts/BaseLayout.vue';
import PrimaryButton from '@/components/PrimaryButton.vue';
import ListPatient from '@/components/ListPatient.vue';
import InfoPatient from '@/components/InfoPatient.vue';

export default {
  name: 'HomeView',
  components: {
    BaseLayout,
    PrimaryButton,
    ListPatient,
    InfoPatient
  },
  data() {
    return {
      persons: [
        { id: 5, nom: "TEST", prenom: "Test", date_naissance: "06/06/1986", lieu_de_naissance: "Lyon", 
        num_secu: "1 03 000 000 0000", num_mutuelle: "0123456789", nom_mutuelle: "Patrick", 
        adresse: "01 rue de Lyon", etat: "", pays: "France", 
        num_telephone: "0606060606", email: "test.test@pmail.com", 
        personneAContacter: {nom_contact: "JEAN", prenom_contact: "Anthony", num_contact: "0707070707"}, 
        autre: {antecedent: "Braquage a main armée", allergie: "Cuivre"} },
        { id: 1, nom: "JEAN", prenom: "Anthony" },
        { id: 2, nom: "SMITH", prenom: "John" },
        { id: 3, nom: "PEYRAR", prenom: "Thibaut" },
        { id: 4, nom: "JOHN", prenom: "Smith" },
      ],
      constantes: [
        { id_patient: "5", frequence_cardiaque: "20", tension: "2", temperature: "38", groupe_sanguin: "O+", poids: "90", taille: "180", date_releve: "05/01/2003" }
      ],
      page: 1
    };
  },
  methods: {
    navBarre(index){
      console.log(index);
      this.page = index
      console.log(this.page);
    }
  }
};
</script>

<template>
  <BaseLayout>
    <div class="grid h-full grid-cols-5 gap-8">
        
          <div class="flex-grow">
            <ListPatient :persons="persons"/>
          </div>

     <!--  <div class="h-full overflow-auto ">
        <InfoComponent :data="persons[selectedRow]" @update:modify="modifyInfo = true" :modify="modifyInfo" :create="createMode"/>
      </div> -->

      <div class="col-span-4 overflow-hidden bg-gradient-to-tr">
        <div class="flex flex-col h-full gap-4 p-4 rounded-md bg-mercury-200">
          
          <div class="flex items-end justify-between">
            <PrimaryButton class="h-fit mx-0.5" @click="navBarre(1)" :buttonClass="{'bg-white bg-image-none text-black':page!=1, 'text-white':page==1}">Informations patient</PrimaryButton>
            <PrimaryButton class="h-fit mx-0.5" @click="navBarre(2)" :buttonClass="{'bg-white bg-image-none text-black':page!=2, 'text-white':page==2}">Examens</PrimaryButton>
            <PrimaryButton class="h-fit mx-0.5" @click="navBarre(3)" :buttonClass="{'bg-white bg-image-none text-black':page!=3, 'text-white':page==3}">Constante</PrimaryButton>
            <PrimaryButton class="h-fit mx-0.5" @click="navBarre(4)" :buttonClass="{'bg-white bg-image-none text-black':page!=4, 'text-white':page==4}">Prescription</PrimaryButton>
          </div>
          
          <div class="h-full p-2 bg-white rounded-md">
            <InfoPatient :person="persons.find(person => person.id=5)"/>
          </div>
          
        </div>
      </div>

    </div>


  </BaseLayout>
</template>
