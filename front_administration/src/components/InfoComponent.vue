<template>
  <div class="flex w-full h-full p-8 overflow-auto bg-white rounded-3xl">
    <div v-if="data || create" class="w-full">
      <div class="flex flex-col w-full gap-2 text-lg" v-if="!modify && !create">
        <div class="flex justify-between">
          <h2 class="text-xl font-bold underline">Patient</h2>
          <PrimaryButton @click="editButton" buttonClass="!shadow-none px-4">
            <EditIcon/>
          </PrimaryButton>
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
        <div class="mt-8 text-center">
          <h3 class="text-xl font-bold underline">Personne à contacter</h3>
        </div>
        <p class="font-semibold">Nom : <span class="font-normal">{{ data.nom_contact }}</span></p>
        <p class="font-semibold">Prénom : <span class="font-normal">{{ data.prenom_contact }}</span></p>
        <p class="font-semibold">Mobile : <span class="font-normal">{{ data.num_contact }}</span></p>
      </div>
      <div class="flex flex-col gap-2 mb-8 text-lg" v-else>
        <div class="flex justify-between">
          <h2 class="text-xl font-bold underline">{{ create ? "Nouveau patient" : "Patient" }}</h2>
          <PrimaryButton buttonClass="!shadow-none">
            Valider
          </PrimaryButton>
        </div>
        <InputComponent id="nom" label="Nom" type="text" v-model="formData.nom" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        <InputComponent id="prenom" label="Prénom" type="text" v-model="formData.prenom" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        <InputComponent id="date_naissance" label="Date de naissance" type="text" v-model="formData.date_naissance" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        <InputComponent id="lieu_de_naissance" label="Lieu de naissance" type="text" v-model="formData.lieu_de_naissance" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        <InputComponent id="num_secu" label="Numéro sécurité sociale" type="text" v-model="formData.num_secu" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        <InputComponent id="num_mutuelle" label="Numéro mutuelle" type="text" v-model="formData.num_mutuelle" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        <InputComponent id="nom_mutuelle" label="Nom mutuelle" type="text" v-model="formData.nom_mutuelle" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        <InputComponent id="adresse" label="Adresse" type="text" v-model="formData.adresse" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        <InputComponent id="code_postal" label="Code postale" type="text" v-model="formData.code_postal" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        <InputComponent id="ville" label="Ville" type="text" v-model="formData.ville" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        <InputComponent id="etat" label="Etat/Province" type="text" v-model="formData.etat" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        <InputComponent id="pays" label="Pays" type="text" v-model="formData.pays" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        <InputComponent id="num_telephone" label="Mobile" type="text" v-model="formData.num_telephone" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        <InputComponent id="email" label="Email" type="text" v-model="formData.email" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        
        <div class="mt-8 text-center">
          <h3 class="text-xl font-bold underline">Personne à contacter</h3>
        </div>
        <InputComponent id="nom_contact" label="Nom" type="text" v-model="formData.nom_contact" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        <InputComponent id="prenom_contact" label="Prénom" type="text" v-model="formData.prenom_contact" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
        <InputComponent id="num_contact" label="Mobile" type="text" v-model="formData.num_contact" input-class="border-gray-200 shadow-none bg-neutral-200 focus:border-gray-300" />
      </div>
    </div>
    <div class="flex items-center justify-center w-full" v-else>
      <p class="w-fit">Veuillez sélectionner un patient pour voir ces informations.</p>
    </div>
  </div>
</template>

<script>
import PrimaryButton from './PrimaryButton.vue';
import EditIcon from './icons/EditIcon.vue';
import InputComponent from './InputComponent.vue';

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
  components : {
    PrimaryButton,
    EditIcon,
    InputComponent
  },
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