# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Card.played'
        db.add_column('deckocards_card', 'played',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Card.rank'
        db.alter_column('deckocards_card', 'rank', self.gf('django.db.models.fields.CharField')(max_length=12))

        # Changing field 'Card.suit'
        db.alter_column('deckocards_card', 'suit', self.gf('django.db.models.fields.CharField')(max_length=12))
    def backwards(self, orm):
        # Deleting field 'Card.played'
        db.delete_column('deckocards_card', 'played')


        # Changing field 'Card.rank'
        db.alter_column('deckocards_card', 'rank', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Card.suit'
        db.alter_column('deckocards_card', 'suit', self.gf('django.db.models.fields.CharField')(max_length=10))
    models = {
        'deckocards.card': {
            'Meta': {'object_name': 'Card'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'played': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rank': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'suit': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        }
    }

    complete_apps = ['deckocards']