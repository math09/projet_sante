<template>
  <div class="bg-white p-8 rounded-3xl h-full flex overflow-auto w-full">
    <div v-if="data || create" class="w-full">
      <div class="flex flex-col gap-2 text-lg w-full" v-if="!modify && !create">
        <div class="flex justify-between">
          <h2 class="font-bold text-xl underline">Patient</h2>
        </div>
        <p class="font-semibold">Nom : <span class="font-normal">{{ data.nom }}</span></p>
        <p class="font-semibold">Prénom : <span class="font-normal">{{ data.prenom }}</span></p>
        <div class="grid grid-cols-2">
          <p class="font-semibold">Date de naissance : <span class="font-normal">{{ data.date_naissance }}</span></p>
          <p class="font-semibold">Age : <span class="font-normal">{{ getAge(data.date_naissance) }}</span></p>
        </div>
        <p class="font-semibold">Lieu de naissance : <span class="font-normal">{{ data.lieu_de_naissance }}</span></p>
        <p class="font-semibold">Numéro sécurité sociale : <span class="font-normal">{{ data.num_secu }}</span></p>
        <p class="font-semibold">Numéro mutuelle : <span class="font-normal">{{ data.num_mutuelle }}</span></p>
        <p class="font-semibold">Nom mutuelle : <span class="font-normal">{{ data.nom_mutuelle }}</span></p>
        <p class="font-semibold">Adresse : <span class="font-normal">{{ data.adresse }}</span></p>
        <div class="grid grid-cols-2">
          <p class="font-semibold">Code postale : <span class="font-normal">{{ data.code_postal }}</span></p>
          <p class="font-semibold">Ville : <span class="font-normal">{{ data.ville }}</span></p>
        </div>
        <p class="font-semibold">Etat/Province : <span class="font-normal">{{ data.etat }}</span></p>
        <p class="font-semibold">Pays : <span class="font-normal">{{ data.pays }}</span></p>
        <p class="font-semibold">Mobile : <span class="font-normal">{{ data.num_telephone }}</span></p>
        <p class="font-semibold">Email : <span class="font-normal">{{ data.email }}</span></p>
        <div class="text-center mt-8">
          <h3 class="font-bold text-xl underline">Personne à contacter</h3>
        </div>
        <p class="font-semibold">Nom : <span class="font-normal">{{ data.nom_contact }}</span></p>
        <p class="font-semibold">Prénom : <span class="font-normal">{{ data.prenom_contact }}</span></p>
        <p class="font-semibold">Mobile : <span class="font-normal">{{ data.num_contact }}</span></p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    data: {
      type: Object,
      required: false
    },
    modify: {
      type: Boolean,
      required: false,
      default: false
    },
    create: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  methods: {
    isLastRow(index, length) {
      return index === length - 1;
    },
    selectRow(index) {
      this.$emit('row-selected', index);
    },
    getAge(_date){
      if(!_date) return ''
      const date = new Date(_date);
      const today = Date.now();
      
      const diff = Math.abs(today - date);
      const diffYears = Math.ceil(diff / (1000 * 3600 * 24 * 365.25));
      
      return Math.floor(diffYears).toString + " ans"
    },
    editButton(){
      this.$emit('update:modify');
      this.formData = this.data
    }
  },
  data() {
    return {
      formData: {}
    };
  },
  components : { },
  watch: {
    data: {
      handler(newValue) {
        if (this.create) {
          this.formData = {};
        } else {
          this.formData = newValue;
        }
      },
      immediate: true
    }
  }
};
</script>