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
        { id: 1, nom: "JEAN", prenom: "Anthony", age: "10/05/2003 (20 ans)", numSecu: "1 03 59 034 456" },
        { id: 2, nom: "SMITH", prenom: "John", age: "10/05/2003 (25 ans)", numSecu: "1 02 38 932 678" },
      ],
      selectedRow: null
    };
  },
  methods: {
    searchInDb() {
      console.log('Search:', this.search);
    },
    onRowSelected(index) {
      this.selectedRow = index;
    }
  }
};
</script>

<template>
  <BaseLayout>
    <div class="grid grid-cols-3 gap-4 h-full">
      <div class="col-span-2 overflow-hidden">
        <div class="flex flex-col h-full">
          <div class="flex justify-between  items-end">
            <InputComponent id="search" label="Rechercher" type="text" class="w-[50%]" v-model="search" @input-c="searchInDb" input-class="bg-neutral-200 border-gray-200 focus:border-gray-300 shadow-none">
              <SearchIcon/>
            </InputComponent>
            <PrimaryButton class="h-fit" buttonClass="!shadow-none">Nouveau</PrimaryButton>
          </div>
        
          <div class="mt-10 flex-grow overflow-auto">
            <TableComponent :persons="persons" :selected-row="selectedRow" @row-selected="onRowSelected"/>
          </div>
        </div>
        
      </div>
      <div>
        <InfoComponent/>
      </div>
    </div>


  </BaseLayout>
</template>
