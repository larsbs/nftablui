import Ember from 'ember';

export default Ember.Controller.extend({
  newRuleExpressionIndex: 0,  // Default value
  ruleExpressions: [
    {
      index: 0,
      expression: { id: 'meta', label: 'Meta' },
      keys: [
        { id: 'length', label: 'Longitud del paquete' },
        { id: 'protocol', label: 'Protocolo' },
        { id: 'priority', label: 'Prioridad del paquete' },
        { id: 'mark', label: 'Marca del paquete' },
        { id: 'iif', label: 'Índice de la interfaz de entrada' },
        { id: 'iffname', label: 'Nombre de la interfaz de entrada' },
        { id: 'ifftype', label: 'Tipo de la interfaz de entrada' },
        { id: 'oif', label: 'Índice de la interfaz de salida' },
        { id: 'oifname', label: 'Nombre de la interfaz de salida' },
        { id: 'ofitype', label: 'Tipo de hardware de la interfaz de salida' },
        { id: 'skuid', label: 'UID asociada al socket de origen' },
        { id: 'skgid', label: 'GID asociada al socket de origen' },
        { id: 'rtclassid', label: 'Reino de enrutamiento' },
      ]
    },
    {
      index: 1,
      expression: { id: 'ether', label: 'Ethernet' },
      keys: [
        { id: 'daddr', label: 'Dirección MAC de destino' },
        { id: 'saddr', label: 'Dirección MAC de origen' },
        { id: 'type', label: 'EtherType' },
      ]
    },
    {
      index: 2,
      expression: { id: 'vlan', label: 'VLAN' },
      keys: [
        { id: 'id', label: 'VLAN ID (VID)' },
        { id: 'cfi', label: 'Indicador de formato canónico' },
        { id: 'pcp', label: 'Punto de código de prioridad' },
        { id: 'type', label: 'EtherType' },
      ]
    },
    {
      index: 3,
      expression: { id: 'arp', label: 'ARP' },
      keys: [
        { id: 'htype', label: 'Tipo de hardware ARP' },
        { id: 'ptype', label: 'EtherType' },
        { id: 'hlen', label: 'Longitud de la dirección hardware' },
        { id: 'plen', label: 'Longitudo de la dirección del protocolo' },
        { id: 'op', label: 'Operación' },
      ]
    },
    {
      index: 4,
      expression: { id: 'ip', label: 'IPv4' },
      keys: [
        { id: 'version', label: 'Versión de la cabecera IP' },
        { id: 'hdrlength', label: 'Longitud de la cabecera IP (incluye opciones)' },
        { id: 'tos', label: 'Tipo de servicio' },
        { id: 'length', label: 'Longitud del paquete' },
        { id: 'id', label: 'ID de la IP' },
        { id: 'frag-off', label: 'Offset del framento' },
        { id: 'ttl', label: 'Tiempo de vida' },
        { id: 'protocol', label: 'Protocolo de la capa superior' },
        { id: 'checksum', label: 'Checksum de la cabecera IP' },
        { id: 'saddr', label: 'Dirección de origen' },
        { id: 'daddr', label: 'Dirección de destino' },
      ]
    },
    {
      index: 5,
      expression: { id: 'ip6', label: 'IPv6' },
      keys: [
        { id: 'version', label: 'Versión de la cabecera IP' },
        { id: 'flowlabel', label: 'Etiqueta de flujo' },
        { id: 'length', label: 'Longitud del campo de datos' },
        { id: 'nexthdr', label: 'Cabecera siguiente' },
        { id: 'hoplimit', label: 'Límite de saltos' },
        { id: 'saddr', label: 'Dirección de origen' },
        { id: 'daddr', label: 'Dirección de destino' },
      ]
    },
    {
      index: 6,
      expression: { id: 'tcp', label: 'TCP' },
      keys: [
        { id: 'sport', label: 'Puerto de origen' },
        { id: 'dport', label: 'Puerto de destino' },
        { id: 'sequence', label: 'Número de secuencia' },
        { id: 'ackseq', label: 'Número de acuse de recibo' },
        { id: 'doff', label: 'Offset de los datos' },
        { id: 'reserved', label: 'Area reservada' },
        { id: 'flags', label: 'TCP Flags' },
        { id: 'window', label: 'Ventana' },
        { id: 'checksum', label: 'Suma de verificación' },
        { id: 'urgptr', label: 'Puntero urgente' },
      ]
    },
    {
      index: 7,
      expression: { id: 'udp', label: 'UDP' },
      keys: [
        { id: 'sport', label: 'Puerto de origen' },
        { id: 'dport', label: 'Puerto de destino' },
        { id: 'length', label: 'Longitud del mensaje' },
        { id: 'checksum', label: 'Suma de verificación' },
      ]
    },
    {
      index: 8,
      expression: { id: 'udplite', label: 'UDP-Lite' },
      keys: [
        { id: 'sport', label: 'Puerto de origen' },
        { id: 'dport', label: 'Puerto de destino' },
        { id: 'cscov', label: 'Covertura de la suma de verificación' },
        { id: 'checksum', label: 'Suma de verificación' },
      ]
    },
    {
      index: 9,
      expression: { id: 'sctp', label: 'SCTP' },
      keys: [
        { id: 'sport', label: 'Puerto de origen' },
        { id: 'dport', label: 'Puerto de destino' },
        { id: 'vtag', label: 'Etiqueta de verificación' },
        { id: 'checksum', label: 'Suma de verificación' },
      ]
    },
    {
      index: 10,
      expression: { id: 'dccp', label: 'DCCP' },
      keys: [
        { id: 'sport', label: 'Puerto de origen' },
        { id: 'dport', label: 'Puerto de destino' },
      ]
    },
    {
      index: 11,
      expression: { id: 'ah', label: 'Cabecera de autenticación' },
      keys: [
        { id: 'nexthdr', label: 'Protocolo de la cabecera siguiente' },
        { id: 'hdrlength', label: 'Longitud de la cabecera' },
        { id: 'reserved', label: 'Área reservada' },
        { id: 'spi', label: 'Índice del parámetro de seguridad' },
        { id: 'sequence', label: 'Número de secuencia' },
      ]
    },
    {
      index: 12,
      expression: { id: 'esp', label: 'ESP' },
      keys: [
        { id: 'spi', label: 'Índice del parámetro de seguridad' },
        { id: 'sequence', label: 'Número de secuencia' },
      ]
    },
    {
      index: 13,
      expression: { id: 'ipcomp', label: 'IPComp' },
      keys: [
        { id: 'nexthdr', label: 'Protocolo de la cabecera siguiente' },
        { id: 'flags', label: 'Flags' },
        { id: 'cfi', label: 'Índice del parámetro de compresión' },
      ]
    },
    {
      index: 14,
      expression: { id: 'ct', label: 'Conntrack' },
      keys: [
        { id: 'state', label: 'Estado de la conexión (State)' },
        { id: 'direction', label: 'Dirección del paquete respecto a la conexión' },
        { id: 'status', label: 'Estado de la conexión (Status)' },
        { id: 'mark', label: 'Marca de la conexión' },
        { id: 'expiration', label: 'Expiración de la conexión' },
        { id: 'helper', label: 'Asistente asociado a la conexión' },
        { id: 'l3proto', label: 'Protocolo de capa de 3 de la conexión' },
        { id: 'saddr', label: 'Dirección de origen de la conexión para la dirección dada' },
        { id: 'daddr', label: 'Dirección de destino de la conexión para la direción dada' },
        { id: 'protocol', label: 'Protocolo de la capa 4 de la conexión para la dirección dada' },
        { id: 'proto-src', label: 'Protocolo de origen de la capa 4 de la conexión para la direción dada' },
        { id: 'proto-dst', label: 'Protocolo de destino de la capa 4 de la conexión para la direción dada' },
      ]
    }
  ],
  newRuleStatementType: 'hardcoded',  // Default value
  statementType: [
    { id: 'hardcoded', label: 'Directamente' },
    { id: 'set', label: 'Conjunto' },
    { id: 'dictionary', label: 'Diccionario' },
  ],
  newRuleHardcodedArgs: [],

  selectedExpression: function () {
    let i = this.get('newRuleExpressionIndex');
    return this.get('ruleExpressions').objectAt(i);
  }.property('newRuleExpressionIndex'),
  selectedExpressionKeys: function () {
    let keys = this.get('selectedExpression').keys;
    this.set('newRuleKey', keys.objectAt(0).id);  // Default value
    return keys;
  }.property('newRuleExpressionIndex'),
  newRuleStatementHardcoded: function () {
    return this.get('newRuleStatementType') === 'hardcoded';
  }.property('newRuleStatementType'),
  newRuleStatementSet: function () {
    return this.get('newRuleStatementType') === 'set';
  }.property('newRuleStatementType'),
  newRuleStatementDictionary: function () {
    return this.get('newRuleStatementType') === 'dictionary';
  }.property('newRuleStatementType'),

  actions: {
    showAddRuleModal: function () {
      this.get('addRuleModal').send('show');
    },
    showEditModal: function () {
      this.get('editChainModal').send('show');
    },
    showEmptyConfirmationModal: function () {
      this.get('emptyConfirmationModal').send('show');
    },
    showDeleteConfirmationModal: function () {
      this.get('deleteConfirmationModal').send('show');
    },
    removeStatementRow: function (index) {
      this.get('newRuleHardcodedArgs').removeAt(index);
    },
    addStatementRow: function () {
      this.get('newRuleHardcodedArgs').pushObject({ match: this.get('newRuleMatch'), action: this.get('newRuleJumps') });
      // Reset values
      this.set('newRuleMatch', '');
      this.set('newRuleJumps', '');
    },
    saveNewRule: function () {
      this.get('newRuleHardcodedArgs').pushObject({ match: this.get('newRuleMatch'), action: this.get('newRuleJumps') });
      let rule = this.store.createRecord('rule', {
        expression: this.get('selectedExpression').expression.id,
        key: this.get('newRuleKey'),
        chain: this.get('chain')
      });
      if (this.get('newRuleStatementHardcoded')) {
        rule.statements = this.get('newRuleHardcodedArgs').toArray();
      }
      else if (this.get('newRuleStatementSet')) {
        if (this.get('chain.table.sets.length') > 0 && ! this.get('newRuleSetArg')) {
          this.set('newRuleSetArg', this.get('chain.table.sets').objectAt(0).get('name'));
        }
        rule.statements = [{ set: '@' + this.get('newRuleSetArg'), action: this.get('newRuleSetArgActions') }];
      }
      else {
        rule.statements = ['vmap @' + this.get('newRuleDictionaryArg')];
      }
      rule.save()
        .then((model) => {
          // Reset values
          this.set('selectedExpressionIndex', 0);
          this.set('newRuleMatch', '');
          this.set('newRuleJumps', '');
          this.get('newRuleHardcodedArgs').clear();
        })
        .catch((err) => {
          console.log('SAVING RULE ERROR')
          console.log(err);
          rule.deleteRecord();
          Ember.$.notification('error', err.errors.message);
          this.get('newRuleHardcodedArgs').clear();
        });
    },
    emptyChain: function () {
      this.get('chain.rules').toArray().forEach(x => x.destroyRecord());
    },
    deleteChain: function () {
      let chain = this.get('chain');
      let chainTable = this.get('chain.table');
      chain.one('didDelete', () => this.transitionToRoute('table', chainTable));
      chain.destroyRecord();
    }
  }
});
