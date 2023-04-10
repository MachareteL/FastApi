// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

export default async function handler(req, res) {

  if (req.method == 'GET') {
    const batida = await fetch('http://127.0.0.1:8000/')
    const conv = await batida.json()
    // const conv = [
    //   { aluno: 'Lucas Macharete', turma: 'DS5' }, { aluno: 'Fulano de tal', turma: 'Mecatrônica 2 ano' }, { aluno: 'Sicrano de outro', turma: 'DS6' }
    // ]
    res.status(200).json(conv)
  }
}
