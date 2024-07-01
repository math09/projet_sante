<template>
<div class="grid grid-cols-3 h-12 rounded-3xl">
  
  <div class="col-span-3 text-center">
    <h4 class="font-semibold underline"><strong>Information</strong></h4>
  </div>
  <p class="w-auto font-semibold">Nom : <span class="font-normal">{{ person.nom }}</span></p>
  <p class="w-auto font-semibold">Prénom : <span class="font-normal">{{ person.prenom }}</span></p>
  <p class="w-auto font-semibold">Age : <span class="font-normal">{{ getAge(person.date_naissance) }}</span></p>
  
    <p class="w-auto font-semibold">Date de naissance : <span class="font-normal">{{ person.date_naissance }}</span></p>
    <p class="w-auto font-semibold col-span-2">Lieu de naissance : <span class="font-normal">{{ person.lieu_de_naissance }}</span></p>
  
    <p class="w-auto font-semibold">Numéro sécurité sociale : <span class="font-normal">{{ person.num_secu }}</span></p>
    <p class="w-auto font-semibold">Numéro mutuelle : <span class="font-normal">{{ person.num_mutuelle }}</span></p>
    <p class="w-auto font-semibold">Nom mutuelle : <span class="font-normal">{{ person.nom_mutuelle }}</span></p>
  
    <p class="w-auto font-semibold">Adresse : <span class="font-normal">{{ person.adresse }}</span></p>
    <p class="w-auto font-semibold">Etat/Province : <span class="font-normal">{{ person.etat }}</span></p>
    <p class="w-auto font-semibold">Pays : <span class="font-normal">{{ person.pays }}</span></p>
 
    <p class="w-auto font-semibold">Mobile : <span class="font-normal">{{ person.num_telephone }}</span></p>
    <p class="w-auto font-semibold col-span-2">Email : <span class="font-normal">{{ person.email }}</span></p>
  
  <div class="text-center col-span-3">
    <h3 class="font-semibold underline"><strong>Personne à contacter</strong></h3>
  </div>
    <p class="w-auto font-semibold">Nom : <span class="font-normal">{{ person.personneAContacter.nom_contact }}</span></p>
    <p class="w-auto font-semibold col-span-2">Prénom : <span class="font-normal">{{ person.personneAContacter.prenom_contact }}</span></p>
  
    <p class="w-auto font-semibold">Mobile : <span class="font-normal">{{ person.personneAContacter.num_contact }}</span></p>

  <div class="text-center col-span-3">
    <h4 class="font-semibold underline"><Strong>Autre</Strong></h4>
  </div>
  
    <p class="font-semibold">Antécédent : <span class="font-normal">{{ person.autre.antecedent }}</span></p>
  
  
    <p class="font-semibold">Mobile : <span class="font-normal">{{ person.autre.allergie }}</span></p>
  
    <div class="text-center col-span-3">
      <h4 class="w-auto font-semibold underline"><Strong>Dernière constante :</Strong></h4>
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