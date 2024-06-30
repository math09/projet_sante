<template>
<div class="grid h-12 rounded-3xl">
      Person : {{ person }}
  
  <div class="grid-rows-1 text-center">
    <h4 class="font-semibold underline"><strong>Information</strong></h4>
  </div>
  <div class="grid-rows-2">
    <a class="w-auto font-semibold">Nom : <span class="font-normal">{{ person.nom }}</span></a>
    <a class="w-auto font-semibold">Prénom : <span class="font-normal">{{ person.prenom }}</span></a>
    <a class="w-auto font-semibold">Age : <span class="font-normal">{{ getAge(person.date_naissance) }}</span></a>
  </div>
  <div class="grid-rows-3">
    <a class="w-auto font-semibold">Date de naissance : <span class="font-normal">{{ person.date_naissance }}</span></a>
    <a class="w-auto font-semibold">Lieu de naissance : <span class="font-normal">{{ person.lieu_de_naissance }}</span></a>
  </div>
  <div class="grid-rows-4">
    <a class="w-auto font-semibold">Numéro sécurité sociale : <span class="font-normal">{{ person.num_secu }}</span></a>
    <a class="w-auto font-semibold">Numéro mutuelle : <span class="font-normal">{{ person.num_mutuelle }}</span></a>
    <a class="w-auto font-semibold">Nom mutuelle : <span class="font-normal">{{ person.nom_mutuelle }}</span></a>
  </div>
  <div class="grid-rows-5">
    <a class="w-auto font-semibold">Adresse : <span class="font-normal">{{ person.adresse }}</span></a>
    <a class="w-auto font-semibold">Etat/Province : <span class="font-normal">{{ person.etat }}</span></a>
    <a class="w-auto font-semibold">Pays : <span class="font-normal">{{ person.pays }}</span></a>
  </div>
  <div class="grid-rows-6">
    <a class="w-auto font-semibold">Mobile : <span class="font-normal">{{ person.num_telephone }}</span></a>
    <a class="w-auto font-semibold">Email : <span class="font-normal">{{ person.email }}</span></a>
  </div>
  <div class="text-center grid-rows-7">
    <h3 class="font-semibold underline"><strong>Personne à contacter</strong></h3>
  </div>
  <div class="grid-rows-8">
    <a class="w-auto font-semibold">Nom : <span class="font-normal">{{ person.personneAContacter.nom_contact }}</span></a>
    <a class="w-auto font-semibold">Prénom : <span class="font-normal">{{ person.personneAContacter.prenom_contact }}</span></a>
  </div>
  <div class="grid-rows-9">
    <a class="w-auto font-semibold">Mobile : <span class="font-normal">{{ person.personneAContacter.num_contact }}</span></a>
  </div>
  <div class="text-center grid-rows-10">
    <h4 class="font-semibold underline"><Strong>Autre</Strong></h4>
  </div>
  <div class="grid-rows-11">
    <a class="font-semibold">Antécédent : <span class="font-normal">{{ person.autre.antecedent }}</span></a>
  </div>
  <div class="grid-rows-12">
    <a class="font-semibold">Mobile : <span class="font-normal">{{ person.autre.allergie }}</span></a>
  </div>
  <div class="text-center grid-rows-13">
    <h4 class="w-auto font-semibold underline"><Strong>Dernière constante :</Strong></h4>
  </div>
  <div class="grid-rows-14"></div>
  <div class="grid-rows-15"></div>
  <div class="grid-rows-16"></div>
  <div class="grid-rows-17"></div>
  
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
      
      return Math.floor(diffYears).toString + " ans"
    }
  }
};

</script>