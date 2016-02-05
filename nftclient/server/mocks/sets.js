module.exports = function(app) {
  var express = require('express');
  var setsRouter = express.Router();

  var SETS = [
    {
      id: 'qwer',
      name: 'qwer',
      dataType: 'ipv4_addr',
      items: '192.168.1.1,134.123.12.3',
      table: 'ip:ip_lars'
    }
  ];

  setsRouter.get('/', function(req, res) {
    res.send({
      'sets': SETS
    });
  });

  setsRouter.post('/', function(req, res) {
    res.status(201);
    var set = req.body.set;
    set.id = set.name;
    res.send({
      'set': set
    });
  });

  setsRouter.get('/:id', function(req, res) {
    res.send({
      'set': SETS.getById(req.params.id)
    });
  });

  setsRouter.put('/:id', function(req, res) {
    res.send({
      'sets': {
        id: req.params.id
      }
    });
  });

  setsRouter.delete('/:id', function(req, res) {
    res.status(204).end();
  });

  app.use('/api/sets', setsRouter);
};
