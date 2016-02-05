import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr('string'),
  keyDataType: DS.attr('string'),
  valueDataType: DS.attr('string'),
  items: DS.attr('string'),

  keys: function () {
    let keys = [];
    if (this.get('items')) {
      this.get('items').split(',').forEach(e => keys.push(e.split(':')[0]));
    }
    return keys;
  }.property('items'),
  itemsArray: function () {
    if (this.get('items')) {
      return this.get('items').split(',');
    }
    else {
      return [];
    }
  }.property('items'),
  itemsTextarea: function () {
    return this.get('itemsArray').join('\n');
  }.property('items'),

  table: DS.belongsTo('table', {
    async: true
  })
});
