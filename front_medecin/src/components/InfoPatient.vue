<template>
<div class="h-full bg-white rounded-xl">
  <div v-if="person!=undefined || person!=null" class="grid w-full h-full px-8 py-5 overflow-auto h-grid">
    <div class="col-span-3 text-center">
      <h4 class="font-semibold text-xl underline"><strong>Information</strong></h4>
    </div>
      <p class="w-auto font-semibold text-lg">Nom : <span class="font-normal">{{ person.nom }}</span></p>
      <p class="w-auto font-semibold text-lg">Prénom : <span class="font-normal">{{ person.prenom }}</span></p>
      <p class="w-auto font-semibold text-lg">Age : <span class="font-normal">{{ getAge(person.date_naissance) }}</span></p>
    
      <p class="w-auto font-semibold text-lg">Date de naissance : <span class="font-normal">{{ person.date_naissance }}</span></p>
      <p class="w-auto col-span-2 font-semibold text-lg">Lieu de naissance : <span class="font-normal">{{ person.lieu_de_naissance }}</span></p>
    
      <p class="w-auto font-semibold text-lg">Numéro sécurité sociale : <span class="font-normal">{{ person.num_secu }}</span></p>
      <p class="w-auto font-semibold text-lg">Numéro mutuelle : <span class="font-normal">{{ person.num_mutuelle }}</span></p>
      <p class="w-auto font-semibold text-lg">Nom mutuelle : <span class="font-normal">{{ person.nom_mutuelle }}</span></p>
    
      <p class="w-auto font-semibold text-lg">Adresse : <span class="font-normal">{{ person.adresse }}</span></p>
      <p class="w-auto font-semibold text-lg">Etat/Province : <span class="font-normal">{{ person.etat }}</span></p>
      <p class="w-auto font-semibold text-lg">Pays : <span class="font-normal">{{ person.pays }}</span></p>
  
      <p class="w-auto font-semibold text-lg">Mobile : <span class="font-normal">{{ person.num_telephone }}</span></p>
      <p class="w-auto col-span-2 font-semibold text-lg">Email : <span class="font-normal">{{ person.email }}</span></p>
    
    <div class="col-span-3 text-center">
      <h3 class="font-semibold text-xl underline"><strong>Personne à contacter</strong></h3>
    </div>
      <p class="w-auto font-semibold text-lg">Nom : <span class="font-normal">{{ person.nom_contact }}</span></p>
      <p class="w-auto col-span-2 font-semibold text-lg">Prénom : <span class="font-normal">{{ person.prenom_contact }}</span></p>
    
      <p class="w-auto font-semibold text-lg">Mobile : <span class="font-normal">{{ person.num_contact }}</span></p>

    <div class="col-span-3 text-center">
      <h4 class="font-semibold text-xl underline"><Strong>Autre</Strong></h4>
    </div>
    
      <p class="font-semibold text-lg">Antécédent : <span class="font-normal">{{ person.antecedants }}</span></p>
    
    
      <p class="font-semibold text-lg">Allergie : <span class="font-normal">{{ person.allergies }}</span></p>
    
    <div class="col-span-3 text-center" v-if="constante">
      <h4 class="w-auto font-semibold text-xl underline"><Strong>Dernière constante :</Strong></h4>
    </div>
      <p v-if="constante" class="w-auto font-semibold text-lg col-span-3">Date de relevé : <span class="font-normal">{{constante.date_releve || ""}}</span></p>
      <p v-if="constante" class="w-auto font-semibold text-lg">Fréquence cardiaque : <span class="font-normal">{{ constante.frequence_cardiaque || "" }}</span></p>
      <p v-if="constante" class="w-auto  font-semibold text-lg col-span-2">Tension : <span class="font-normal">{{ constante.tension || ""}}</span></p>
      <p v-if="constante" class="w-auto font-semibold text-lg">Température : <span class="font-normal">{{ constante.temperature || ""}}</span></p>
      <p v-if="constante" class="w-auto col-span-2 font-semibold text-lg">Groupe sanguin : <span class="font-normal">{{ constante.groupe_sanguin || ""}}</span></p>
      <p v-if="constante" class="w-auto font-semibold text-lg">Taille (cm): <span class="font-normal">{{ constante.taille || ""}}</span></p>
      <p v-if="constante" class="w-auto font-semibold text-lg">Poids (kg): <span class="font-normal">{{ constante.poids || ""}}</span></p>
      <p v-if="constante" class="w-auto font-semibold text-lg">IMC : <span class="font-normal">{{ (constante.taille/constante.poids)*constante.poids || ""}}</span></p>
  </div>
  
</div>
</template>

<style>
  a{
    padding-left: 5px;
    padding-right: 5px;
    font-size: medium;
  }
</style>

<script>
export default {
  props: {
    person: {
      type: Object,
      required: true
    },
    constante:{
      type: Object,
      required: false
    }
  },
  methods:{
    getAge(_date){
      if(!_date) return ''
      const date = new Date(_date);
      const today = Date.now();
      
      const diff = Math.abs(today - date);
      const diffYears = Math.ceil(diff / (1000 * 3600 * 24 * 365.25));
      
      return Math.floor(diffYears).toString() + " ans"
    }
  }
};

</script>