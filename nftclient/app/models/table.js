import DS from 'ember-data';

export default DS.Model.extend({
  name: DS.attr('string'),
  family: DS.attr('string'),

  verboseName: function () {
    return this.get('family') + ' > ' + this.get('name');
  }.property('name', 'family'),

  chains: DS.hasMany('chain', {
    async: true
  }),
  sets: DS.hasMany('set', {
    async: true
  }),
  dictionaries: DS.hasMany('dictionary', {
    async: true
  })
});
