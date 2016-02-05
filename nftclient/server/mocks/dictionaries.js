module.exports = function(app) {
  var express = require('express');
  var dictionariesRouter = express.Router();

  var DICTIONARIES = [
    {
      id: 'mydict',
      name: 'mydict',
      keyDataType: 'ipv4_addr',
      valueDataType: 'verdict',
      items: '192.168.1.2:counter,192.168.1.3:jump filter_lars,192.168.1.4:drop',
      table: 'ip:ip_lars'
    }
  ];

  dictionariesRouter.get('/', function(req, res) {
    res.send({
      'dictionaries': DICTIONARIES
    });
  });

  dictionariesRouter.post('/', function(req, res) {
    res.status(201).end();
  });

  dictionariesRouter.get('/:id', function(req, res) {
    res.send({
      'dictionaries': DICTIONARIES.getById(req.params.id)
    });
  });

  dictionariesRouter.put('/:id', function(req, res) {
    res.send({
      'dictionaries': {
        id: req.params.id
      }
    });
  });

  dictionariesRouter.delete('/:id', function(req, res) {
    res.status(204).end();
  });

  app.use('/api/dictionaries', dictionariesRouter);
};
