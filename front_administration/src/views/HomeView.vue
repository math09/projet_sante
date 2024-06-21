<script>
import BaseLayout from '@/layouts/BaseLayout.vue';
import InputComponent from '@/components/InputComponent.vue';
import PrimaryButton from '@/components/PrimaryButton.vue';
import SearchIcon from '@/components/icons/SearchIcon.vue';
import InfoComponent from '@/components/InfoComponent.vue';
import TableComponent from '@/components/TableComponent.vue';

export default {
  name: 'HomeView',
  components: {
    BaseLayout,
    InputComponent,
    PrimaryButton,
    SearchIcon,
    InfoComponent,
    TableComponent
  },
  data() {
    return {
      search: '',
      persons: [
        { id: 1, nom: "JEAN", prenom: "Anthony", age: "11/05/2003 (20 ans)", num_secu: "1 03 59 034 456" },
        { id: 2, nom: "SMITH", prenom: "John", age: "10/05/2003 (25 ans)", num_secu: "1 02 38 932 678" },
      ],
      selectedRow: null,
      sortBy: '',
      modifyInfo: false,
      createMode: false
    };
  },
  methods: {
    searchInDb() {
      console.log('Search:', this.search);
    },
    onRowSelected(index) {
      this.selectedRow = index;
      this.modifyInfo = false;
      this.createMode = false;
    },
    sortTable() {
      if (this.sortBy === 'nom') {
        this.persons.sort((a, b) => a.nom.localeCompare(b.nom));
      } else if (this.sortBy === 'prenom') {
        this.persons.sort((a, b) => a.prenom.localeCompare(b.prenom));
      } else if (this.sortBy === 'age') {
        this.persons.sort((a, b) => a.age.localeCompare(b.age));
      }
    },
    newButton(){
      this.selectedRow = null;
      this.createMode = true;
    }
  },
  watch: {
    sortBy() {
      this.sortTable(); // Appel de la fonction de tri lorsque `sortBy` change
    },
  },
};
</script>

<template>
  <BaseLayout>
    <div class="grid grid-cols-3 gap-8 h-full">
      <div class="col-span-2 overflow-hidden">
        <div class="flex flex-col h-full">
          <div class="flex justify-between  items-end">
            <InputComponent id="search" label="Rechercher" type="text" class="w-[50%]" v-model="search" @input-c="searchInDb" input-class="bg-neutral-200 border-gray-200 focus:border-gray-300 shadow-none">
              <SearchIcon/>
            </InputComponent>
            <div class="flex flex-col">
              <label for="sortSelect" class="mb-2 font-semibold text-md">Trier par :</label>
              <select id="sortSelect" v-model="sortBy" class="px-5 py-4 text-md border focus:outline-none rounded-2xl flex-grow bg-neutral-200 border-gray-50 focus:border-gray-300">
                <option value="nom">Nom</option>
                <option value="prenom">Prénom</option>
                <option value="age">Date de naissance</option>
              </select>
            </div>
            <PrimaryButton class="h-fit" buttonClass="!shadow-none" @click="newButton">Nouveau</PrimaryButton>
          </div>
        
          <div class="mt-10 flex-grow overflow-auto">
            <TableComponent :persons="persons" :selected-row="selectedRow" @row-selected="onRowSelected"/>
          </div>
        </div>
        
      </div>
      <div class="h-full overflow-auto">
        <InfoComponent :data="persons[selectedRow]" @update:modify="modifyInfo = true" :modify="modifyInfo" :create="createMode"/>
      </div>
    </div>


  </BaseLayout>
</template>
