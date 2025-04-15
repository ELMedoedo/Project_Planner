from flask import Flask, Blueprint, render_template, flash, redirect, url_for


blueprint = Blueprint("user", __name__, url_prefix="/users")