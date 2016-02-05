import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr('string'),
  dataType: DS.attr('string'),
  items: DS.attr('string'),

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
