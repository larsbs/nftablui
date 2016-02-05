import Ember from 'ember';

export default Ember.Controller.extend({
  newTableFamily: 'ip',  // Default value
  tableFamilies: ['ip', 'ip6', 'inet', 'arp', 'bridge'],
  structureClasses: [
    { id: 'set', name: 'Conjunto' },
    { id: 'dictionary', name: 'Diccionario' }
  ],
  newStructureClass: 'set',  // Default value
  newSetDataType: 'ipv4_addr',  // Default value
  newDictionaryKeyDataType: 'ipv4_addr',  // Default value
  newDictionaryValueDataType: 'verdict',  // Default value
  validSetDataTypes: [
    { id: 'ipv4_addr', name: 'Dirección IPv4' },
    { id: 'ipv6_addr', name: 'Dirección IPv6' },
    { id: 'ether_addr', name: 'Dirección Ethernet' },
    { id: 'inet_proto', name: 'Protocolo INET' },
    { id: 'inet_service', name: 'Servicio INET' },
    { id: 'mark', name: 'Tipo de marca' }
  ],
  validValuesDataTypes: [
    { id: 'verdict', name: 'Veredicto' },
    //{ id: 'ipv4_addr', name: 'Dirección IPv4' },
    //{ id: 'ipv6_addr', name: 'Dirección IPv6' },
    //{ id: 'ether_addr', name: 'Dirección Ethernet' },
    //{ id: 'inet_proto', name: 'Protocolo INET' },
    //{ id: 'inet_service', name: 'Servicio INET' }
  ],

  newStructureTable: function () {
    if (this.get('tables.length') > 0) {
      return this.get('tables').objectAt(0).get('id');
    }
  }.property('tables'),
  addingSet: function () {
    return this.get('newStructureClass') === 'set';
  }.property('newStructureClass'),

  actions: {
    showAddTableModal: function () {
      this.get('addTableModal').send('show');
    },
    showAddStructureModal: function () {
      this.get('addStructureModal').send('show');
    },
    saveNewTable: function () {
      let table = this.store.createRecord('table', {
        family: this.get('newTableFamily'),
        name: this.get('newTableName')
      });
      table.save()
        .then((model) => {
          // Reset table form
          this.set('newTableFamily', 'ip');
          this.set('newTableName', '');
        })
        .catch((err) => {
          table.deleteRecord();
          console.log(err);
          Ember.$.notification('error', err.errors.message);
        });
    },
    saveNewStructure: function () {
      if (this.get('tables.length') > 0 && ! this.get('newStructureTables')) {
        this.set('newStructureTable', this.get('tables').objectAt(0).get('id'));
      }
      if (this.get('newStructureClass') === 'set') {
        this.saveNewSet();
      }
      else {
        this.saveNewDictionary();
      }
    }
  },

  saveNewSet: function () {
    let setItems = this.get('newSetItems');
    if (setItems) {
      setItems = setItems.split('\n');
      setItems.forEach((e, i) => setItems[i] = e.trim());
      setItems = setItems.join();
    }
    else {
      setItems = '';
    }
    let set = this.store.createRecord('set', {
      name: this.get('newSetName'),
      dataType: this.get('newSetDataType'),
      table: this.store.peekRecord('table', this.get('newStructureTable')),
      items: setItems
    });
    set.save()
      .then((model) => {
        // Reset structure form
        this.set('newStructureClass', 'set');
        this.set('newSetName', '');
        this.set('newSetDataType', 'ipv4_addr');
        this.set('newSetItems', '');
      })
      .catch((err) => {
        set.deleteRecord();
        console.log(err);
        Ember.$.notification('error', err.errors.message);
      });
  },
  saveNewDictionary: function () {
    let dictionaryItems = this.get('newDictionaryItems');
    if (dictionaryItems) {
      dictionaryItems = dictionaryItems.split('\n');
      dictionaryItems.forEach((e, i) => dictionaryItems[i] = e.trim());
      dictionaryItems = dictionaryItems.join();
    }
    else {
      dictionaryItems = '';
    }
    let dictionary = this.store.createRecord('dictionary', {
      name: this.get('newDictionaryName'),
      keyDataType: this.get('newDictionaryKeyDataType'),
      valueDataType: this.get('newDictionaryValueDataType'),
      table: this.store.peekRecord('table', this.get('newStructureTable')),
      items: dictionaryItems
    });
    dictionary.save()
      .then((model) => {
        // Reset structure form
        this.set('newStructureClass', 'set');
        this.set('newDictionaryName', '');
        this.set('newDictionaryKeyDataType', 'ipv4_addr');
        this.set('newDictionaryValueDataType', 'verdict');
        this.set('newDictionaryItems', '');
      })
      .catch((err) => {
        dictionary.deleteRecord();
        console.log(err);
        Ember.$.notification('error', err.errors.message);
      });
  }
});
